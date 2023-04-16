import multiprocessing
import os


def login():
    print("登录成功")
    print("当前线程:" , multiprocessing.current_process())


def login_arg(name, password):
    print(F"用户名:{name}, 密码：{password}")
    print(F"当前线程:{multiprocessing.current_process()}")
    print(F"当前进程pid:{os.getpid()}")
    print(F"当前进程父进程pid:{os.getppid()}")


if __name__ == '__main__':
    '''
        group: 组名
        target: 任务名
        name: 进程名
        arg kwargs 参数
        daemon 是否是守护进程
    '''

    t1 = multiprocessing.Process(target=login_arg,name="worker1",args=("田坤",123456))
    t2 = multiprocessing.Process(target=login_arg,name="worker2",args=("田坤","123456789"))
    t3 = multiprocessing.Process(target=login_arg,name="worker3",kwargs={"name": "田坤","password": "123"})

    t1.start()
    t2.start()
    t3.start()
    print(F"主进程pid:{os.getpid()}")