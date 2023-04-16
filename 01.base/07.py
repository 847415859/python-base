
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

for i in list2:
    print(i)


for i in enumerate(list2):
    print(type(i))
    print(i[0])
    print(i)

# 推导式
# [要插入列表的表达式 for 临时变量 in 数据序列]

list1 =[1 for i in range(1,100) if i % 2 == 0]
print(list1)


list2 = []

for i in range(1,10):
    for j in range(1, i + 1):
        print(F"{i} * {j} = {i * j}",end='  ')
        list2.append(F"{i} * {j} = {i * j}")
    print()
print(list2)