#
# str = '12345678'
# chinaStr =  '我爱派森'
#
# for s in str:
#     if s == "1":
#         print("= 1")
#     elif s == 2:
#         print("= 2")
#     else:
#         print(s)
#
#
# for s in chinaStr:
#     print(s)
#
#
# for i in range(1,3):
#     print(i)







i = 0
while i <= 100:
    if i == 60:
        print('下载非法文件,已经将你举报,下载终止')
        # break  # 会造成循环异常终止,不会执行else中的代码
        i += 1
        break  # 不会造成循环异常终止,会执行else中的代码
    print(f'下载进度:{i}%')
    i += 1
else:
    print('下载完成')


# 需求:打印五行五列的一个*组成的矩形
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
i = j = 0
while i < 5:
    j = 0
    while j < 5:
        print("*",end=" ")
        j += 1
    i += 1
    print("")

# 使用while循环的嵌套打印九九乘法表
"""
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
.......
"""

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {i*j}" ,end=" ")
        j += 1
    print()
    i += 1


str1 = 'helloPython'
for i in str1:
    print(i)

