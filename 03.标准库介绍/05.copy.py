import copy


def deep_test():
    a1 = 123123
    b1 = copy.copy(a1)
    print(id(a1))
    print(id(b1))
    a2 = "abc"
    b2 = copy.copy(a2)
    # 查看内存地址
    print(id(a2))
    print(id(b2))
    a3 = (1, 2, ["hello", "world"])
    b3 = copy.copy(a3)
    # 查看内存地址
    print(id(a3))
    print(id(b3))
    print("-" * 50 + "不可变类型" + "-" * 100)
    a1 = [1, 2]
    b1 = copy.copy(a1)
    print(id(a1))
    print(id(b1))
    a4 = [1, 2, [4, 5]]
    # 注意：浅拷贝只会拷贝父对象，不会对子对象进行拷贝
    b4 = copy.copy(a4)  # 使用copy模块里的copy()函数就是浅拷贝了
    print(id(a4))
    print(id(b4))
    print(id(a4[2]))
    print(id(b4[2]))

def deep_copy():
    a1 = 1
    b1 = copy.deepcopy(a1)  # 使用copy模块里的deepcopy()函数就是深拷贝了
    # 查看内存地址
    print(id(a1))
    print(id(b1))
    print("-" * 10)


if __name__ == '__main__':
    deep_copy()

