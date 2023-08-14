
def func1(*args):
    print(type(args))
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


def func2(a, b, c=10, *args):
    print(a)
    print(b)
    print(c)
    print(args)

func2(1, 2, 3, 4, 5)

def func3(a, b, *args, c=10):
    print(a)
    print(b)
    print(c)
    print(args)
func3(1, 2, 3, 4, 5)


# 注意:字典可以拆包么?可以
dict1 = {'a': 1, 'b': 2, 'c': 3}
# 对字典进行拆包,得到的是字典的键
char1, char2, char3 = dict1
print(char1, char2, char3)

set1 = {'Tom', 'Bob', 'Rose'}
a, b, c = set1
print(a, b, c)


print("=" * 300)
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
list1 = [1, 2, 3, 4, 5]
list2 = list1
list1.pop(2)
list1 + list2
# list1 和list2  分别是多少
print(list1)
print(list2)


# 练习:
str1 = '12345'
str2 = '12345'
str1 = str2
str1 = '123'
str2 + str1
print(str1)
print(str2)
