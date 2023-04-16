
def func1(*args):
    print(args)

func1(1,2,3)


def func2(**kwargs):
    print(kwargs)

func2( a = 1,b = 2)


# 函数定义和调用时各类参数的排布顺序f
# 位置参数 、 位置不定长参数 、 缺省参数 、 关键字不定长参数

def func3(a, b, *args, c = 10, **kwargs ):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

func3(1,2,3,4,5,c= 10, name = "田坤", size = 170)


a = 1
b = "2"
print(id(a))
print(id(b))