import json
import socket
import threading


class WebServer():

    def __init__(self):
        # 1、创建服务端对象
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2、绑定ip和端口
        self.server.bind(('localhost', 8001))
        # 3、监听
        self.server.listen(5)

    def clinet_request(self, clinet_data):
        # 接受客户端（浏览器）数据
        recv_data = clinet_data.recv(1024)
        # 解决方案一 提前判断数据是为空
        # if len(recv_data) == 0:
        #     clinet_data.send('not data')
        # 解决方案二,捕获数据处理异常，捕获到异常就结束函数的业务逻辑执行
        try:
            # 读取请求报文中的请求路径，根据不同的请求路径返回不同的页面
            # 1、将bytes类型转为字符串
            str_data = recv_data.decode()
            # 2、字符串切割 按照\r\n进行切割  得到请求行、请求头数据、请求体数据   GET /register HTTP/1.1\r\nHost: 127.0.0.1:8009\r\nConnection: keep-alive\r\n
            data_list = str_data.split('\r\n')
            print(data_list)
            # 3、从切割后的列表中提取请求行数据 ，再次按照空格切割请求行数   GET /register HTTP/1.1
            request_line = data_list[0]
            # 4、从切割后的请求行列表数据中提取请求路径
            url_path = request_line.split(' ')[1]

        except Exception as e:
            # 输出异常信息
            print(e)
            clinet_data.send(b'not data')
            return None
        # 5、根据不同的请求路径读取不同的页面文件数据返回浏览器
        if url_path == '/users':
            data_json = {'name':'田坤','age':18}
            send_data = json.dumps(data_json)
        elif url_path == '/goods':
            send_data = '/goods'
        else:
            send_data = 'error'

        # 构建报文数据
        # 响应行
        response_line = 'HTTP/1.1 200 ok\r\n'
        # 响应头
        response_header = 'Server:itcast\r\n\r\n'
        # 响应体
        response_body = send_data

        respose_data = response_line + response_header + response_body

        clinet_data.send(respose_data.encode())
    def start(self):

        # 循环等待客户端连接
        print('服务器启动。。。')
        while True:
            clinet_data, addr = self.server.accept()
            print('请求的客户端：', clinet_data)
            # 创建线程处理客户端请求
            t = threading.Thread(target=self.clinet_request, args=(clinet_data,))
            # 启动线程
            t.start()


web = WebServer()
web.start()

