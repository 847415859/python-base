import socket
import threading
import dynamic.frame

class HttpWebServer:

    def __init__(self) -> None:
        # 1.编写一个TCP服务端程序
        # 创建socekt
        self.tcp_server_socekt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口复用　
        self.tcp_server_socekt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定地址 ip地址替换为自己电脑的ip
        self.tcp_server_socekt.bind(("localhost", 8000))
        # 设置监听
        self.tcp_server_socekt.listen(128)

    def handle_client_request(self, client_socekt, client_addr):
        # 获取浏览器的请求信息
        client_request_data = client_socekt.recv(1024).decode()

        # 判断客户端是否关闭
        if len(client_request_data) == 0:
            print('客户端关闭')
            client_socekt.close()
            return

        # 获取用户请求信息
        request_data = client_request_data.split("\r\n")

        # 获取请求行数据
        request_line = request_data.pop(0)  # 使用pop将请求行数据从列表中取出
        request_line_data = request_line.split(' ')

        # 获取请求头部数据
        request_header = {}
        for data in request_data:
            if data == '':
                continue
            request_header[data.split(": ")[0]] = data.split(": ")[1]

        # 将客户端ip地址添加到header中
        request_header['client_addr'] = client_addr

        # 请求行中获取请求资源的路径
        request_path = request_line_data[1]

        # 判断是否有查询字符串数据
        request_query = request_path.split('?')
        if len(request_query) > 1:
            request_path = request_query[0]
            query_str = request_query[1]
        else:
            query_str = None

        # 构造请求数据
        requests = {
            'path': request_path,
            'query_str': query_str,
            'header': request_header,

        }

        """动态资源"""
        # 符合wsgi协议的参数
        env = {
            "request_path": request_path,
            "requests": requests
        }

        # 应答行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 应答头
        response_header = "Server:pwb\r\nAccess-Control-Allow-Credentials:true\r\nAccess-Control-Allow-Origin:*\r\nAccess-Control-Allow-Methods:GET, POST, PUT\n\rAccess-Control-Allow-Headers:X-Custom-Header"
        # 应答体
        response_body = dynamic.frame.application(env)
        # 应答数据
        response_data = response_line + response_header + "\r\n\r\n" + response_body
        # 发送数据给到浏览器
        client_socekt.send(response_data.encode())

        # 关闭和浏览器通讯的socket
        client_socekt.close()

    def start(self):
        while True:
            # 2.获取浏览器发送的HTTP请求报文数据
            # 建立链接
            client_socekt, client_addr = self.tcp_server_socekt.accept()
            # 创建子线程
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socekt, client_addr))
            sub_thread.start()


if __name__ == '__main__':
    my_web_server = HttpWebServer()
    my_web_server.start()
