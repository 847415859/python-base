class Father(object):
    def dance(self):
        print('我现在要跳一个舞,赶紧出去')

    def sing(self):
        print('我要唱一个学猫叫,一起来')


class Mother(object):
    def dance(self):
        print('我现在要跳一个广场舞,离我远点,不然摔倒了赖你')

    def sing(self):
        print('我要唱一个大河向东流,赶紧跑')


# 同时继承两个父类,则在使用子类对象时可以调用两个父类中的所有非私有属性和方法
class Son(Father, Mother):
    pass


s1 = Son()

s1.dance()
s1.sing()