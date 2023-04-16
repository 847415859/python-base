from typing import Type


class Student(object):

    def __init__(self) -> None:
        super().__init__()
        print("执行Init方法")

    def __init__(self,name,age) -> None:
        super().__init__()
        print("带参数执行Init方法")
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def __del__(self):
        print("执行了销毁方法")


def test1():
    s1 = Student()
    print(s1)
    print(type(s1))
    s1.eat()
    s1.sleep()
    s1.name = 1
    print(s1.__dict__)
    del s1.name
    print(s1.__dict__)
    s2 = Student()
    print(s2.__dict__)
    print("=============")
    s2.__init__()


if __name__ == '__main__':
    s2 = Student("田坤",24)
    print(s2.name)

    del s2

    # s3 = Student()
    # s3.eat()

    print(Student.__mro__)
