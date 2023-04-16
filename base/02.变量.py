# int  整型
v1 = 1
print(type(v1))
# float 浮点型
v2 = 1.1
print(type(v2))
# bool 布尔型
v3 = True
print(type(v3))
# str  字符型  字符串
v4 = 'aaa'
v5 = "bbb"
# print(type(v4 + 1))
print(type(v5))
# list  列表
v6 = [1,2,3,4]
print(v6.append(3))
print(type(v6))
# tuple 元组
v7 = (1,2,3,4,5)
print(type(v7))
print((v7))
# set  集合
v8 = {1,2,3,4,5,6}
print(v8)
print(type(v8))
# dict  字典
v9 = {"name": "田坤","age": 18}
print(type(v9))
print(v9)


print("字符串输出格式化 %s" %(v1))
print("字符串输出格式化 %s" % v1)
print("字符串输出格式化 %s， %s" % (v1, v4))


print("aaaa",end='')
print("bbb",end='')