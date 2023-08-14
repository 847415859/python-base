# 装饰器： 给已有函数增加额外功能的函数，它本质上就是一个闭包函数。
# 装饰器的功能特点:
# 不修改已有函数的源代码
# 不修改已有函数的调用方式
# 给已有函数增加额外的功能
def check(func):
    def inner(*args):
        print("请先登录")
        # print(type(args))
        # lst1 = list(args)
        func(args)
    return inner


@check
def common(*args):
    print(f"发表评论：{'❤'.join(args[0])}")


common("a","b","c")

# f = check(common)
# f("a","b","c")

