
list1 =[]

for i in range(1,10):
    list1.append(i)

print(list1)

list2 = [i for i in range(1,10)]
print(list2)


# 练习:
# 用推导式进行九九乘法表的生成,将所有的算式放入列表中
list6 = []
for i in range(1, 10):
    for j in range(1, i + 1):
        list6.append(f'{j} * {i} = {j * i}')

print(list6)

list7 = [f'{j} * {i} = {j * i}' for i in range(1,10) for j in range(1, i + 1)]
print(list7)