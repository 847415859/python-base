def func(num_list):
    print(id(num_list))  # 140490414045760
    num_list.append(2)
    return num_list


# 在进行参数传递时,是进行了地址传递,将list1 的引用地址传递给了num_list,num_list 修改内存空间中的数据时,list1,也会发生变化
list1 = [1, 2, 3, 4]
print(id(func(list1)))
print(list1)
print(id(list1))
