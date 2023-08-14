# F-string
import random

name = "田坤"
age = 24
height = 1.825
no = 1001

print("姓名:%s, 年龄: %d , 身高: %.2f ,学号 %06d" %(name,age,height,no))

print(F"姓名:{name}, 年龄: {age} , 身高: {height:.2f} ,学号 {no:06d}")


print(1 if age > 24 else 2)



v1 = '19'
v2 = '192.2'
v3 = 192.2

print(int(v1))
print(int(float(v2)))
print(int(v3))


print("次幂计算")
print(2**3)
print(3//2)
# 在除法运算中，结果肯定为小数
print(9/3)
print(0.1 + 0.2)

print(1,2,3,4,5,6)


# 比较运算符可以连续使用(Python中的特性)
age = 13
print(12 < age < 30)  # True
# 不等号也可以连续使用
print(12 < age == 13)  # False


'''
    逻辑运算符
'''
print("========逻辑运算符=============")
print(not (True and False))


'''
    短路运算
'''
print(False or "aa")




print(random.randint(1,100))


'''
    三目运算符
'''
age = 13
print("你好" if age != 13 else "我不好")

# age = int(input('请输入对方的年龄:'))
#
# if age > 100 or age < 0:
#     print('数据错误')
# elif 0<= age <= 18:
#     print('小妹妹你真可爱')
#     print('叔叔 我们不约而同的认为我很可爱')
# elif 18< age <= 30:
#     print('美女,你真漂亮')
#     print('流氓')
# elif 30 < age <= 60:
#     print('阿姨,我不想努力了')
#     print('瞧你长那样')
# else:
#     print('老奶奶,您真慈祥')
#     print('我北京三套房')


