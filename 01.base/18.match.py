from enum import Enum


def matchSimple():
    status = 5
    match status:
        case 1:
            print("我是1")
        case 2 | 4:
            print("我是2")
        # 匹配多个 case
        case 3 | 5:
            print("我是3")
        case _:
            print("只要匹配不到那么我就能获取到")


def matchTuple():
    status = (0, 0)
    match status:
        case (0, 0):
            print("元祖三： 都为0")
        case (0, y):
            print(f"元祖一： y = {y}")
        case (x, 0):
            print(f"元祖二： x = {x}")
        case (x, y):
            print(f"元组四： x = {x}, y={y}")
        case _:
            print("无奈之举")



class Status(Enum):
    PASS = 'pass'
    FAIL = 'fail'

if __name__ == '__main__':
    for item in range(1,10,2):
        print(item)