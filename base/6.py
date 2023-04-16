num_list = [1, 2, 3, 4, 5, 6, 7, 8, 5]

print(num_list.count(5))

print('5' in num_list)

num_list.extend('abc')

print(num_list)

# sort  排序
list2 = [2, 6, 43, 2, 41, 421]
# sort是对原有的数据进行了排序,没有产生新的列表.同时,默认排序规则为升序
# print(list2.sort())  # None
# print(list2)  # [2, 2, 6, 41, 43, 421]
# 如果我想让列表降序排列怎么办?
# 方法一:可以先排序再反转
# list2.sort()
# list2.reverse()
# print(list2)  # [421, 43, 41, 6, 2, 2]
# 方法二: 可以直接使用倒叙排列
# list2.sort(reverse=True)  # [421, 43, 41, 6, 2, 2]
# print(list2)

# list2.sort(key=排序规则函数)可以帮助我们进行更加复杂的排序
# 根据每个元素 % 7 的余数大小进行排序
# 了解, 不要求掌握 后续会讲
list2.sort(key=lambda x: x % 7)
print(list2)

dictv = {"name": "田坤", "age": 18}
# print(dictv)
# dictv["height"] = 182.5
# print(dictv)
# del dictv["age"]
# print(dictv)
#
# print(dictv.pop("name"))
# print(dictv.popitem())
# print(dictv)

# dictv.update({"name","田坤1"})
dictv.update(name="田坤1")
print(dictv)

print(dictv.keys())

for key in dictv.keys():
    print(F"key:{key}, value: {dictv.get(key)}")

print(dictv.items())

print("===========================")
for dic in dictv:
    print(dic)


# 获取字典中的key和value

for key,value in dictv.items():
    print(F"键：{key}, 值:{value}")



setv = {1,2,3,4,5,5,55,5,5}
print(setv)

