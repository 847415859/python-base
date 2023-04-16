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




'''
    逻辑运算符
'''

print(not (True and False))


'''
    短路运算
'''
print(False or "aa")




print(random.randint(1,100))


#
#
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