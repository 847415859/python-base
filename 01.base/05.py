str = "python"
str1= str[1:4:2]
print(str1)


# 切片逻辑
# 起始位置: 字符串切片的起点(包含)
# 结束位置:字符串切片的终点(不包含)
# 在开发中绝大多数范围区间是左闭右开区间,其余内容单独记忆(例如 randint是一个闭区间)
# 步长:步长就是每一次查找数据的间隔(相邻两个索引的差值就是步长)

str2 = '我爱北京天安门,天安门上太阳升!'
# 获取"北京天安门"
print(str2[2:7:1])
# 如果步长为1 可以被省略
# 步长省略后,:也可以省略
print(str2[2:7])


# 起始位置也可以省略
# 如果起始位置省略,步长为正数,则起始位置为字符串开始
print(str2[:7:1])  # 我爱北京天安门
# 如果起始位置省略,步长为负数,则起始位置为字符串末尾
print(str2[:7:-1])  # !升阳太上门安天
# 为什么为空?  字符串切片起点是索引为2的位置, 步长是-1  切片区间[2,7),此时从2的位置从右向左步长为1切片此区域没有数据
print(str2[2:7:-1]) # 空字符串
# 结论: 如果步长是负数,开始位置要在结束位置右侧,否则没有数据


splitStr = "1 2 3 4 56- 1,32324 45435 "
splitlist = splitStr.split()
# splitStr.replace()



print(type(splitlist))

print("❤".join(splitlist))

# 翻转
print(str2[::-1])
# 复制
print(str2[:])

print(str2.index("我"))
print("1111")

str1 = 'hello woRld aNd Python'
print(str1.title())
str2 = 'hello中国python'
print(str2.title())

str1.end





