import threading


def func(arg1,arg2):
    print("执行了该方法")
    print(F"当前执行的线程为：{threading.current_thread().name}")



if __name__ == '__main__':
    t1 = threading.Thread(group=None, target=func ,args=(1,"2"),name="t1")
    t2 = threading.Thread(group=None, target=func ,args=(1,"2"),name="t2")
    t3 = threading.Thread(group=None, target=func ,args=(1,"2"),name="t3")
    t1.start()
    t2.start()
    t3.start()
    t1.daemon = True
    print("主线程运行")