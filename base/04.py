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