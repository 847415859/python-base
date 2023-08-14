
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

for i in list2:
    print(i)

print(f"长度 :{len(list2)}")
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

print("="*200)
tuple6 = 5,
print(tuple6)
print(type(tuple6))

tuple7 = (1,2,3,)
print(tuple7)
print(type(tuple7))


dict2 = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

v1 = dict2.pop("name")
print(v1)
print(type(v1))
print(dict2)

v2 = dict2.popitem()
print(v2)
print(type(v2))
print(dict2)

set0 = {1}
set1 = set()
print(type(set0))
print(set1)
print(type(set1))

list2 = [1, 2, 3, 4, 5, 6, 7, 8]
print("*" * 300)
# for i in enumerate(list2):
#     print(i[0])
#     print(i.))
#     print(i)

for index, value in enumerate(list2):
    print(index, value, sep=' : ')