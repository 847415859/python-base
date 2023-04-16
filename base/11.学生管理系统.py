# 需求拆分:
'''
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
'''


def print_all_option():
    """用户功能界面展示"""
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员信息')
    print('2: 删除学员信息')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 遍历输出所有学员信息')
    print('6: 退出系统')
    print('-' * 20)

# 姓名集合
nameDict = {}
# 学号集合
idDict = {}

def oprAdd():
    print("输入学号:",end=' ')
    id = input()
    print("输入姓名:",end=' ')
    name = input()
    print("输入你的其他信息:")
    otherInfo = {}
    while True:
        other =  input()
        if other.strip() == "q":
            break
        info = other.split()
        otherInfo[info[0]] = info[1]
    add(id,name,otherInfo)


def add(id,name,otherInfo):
    nameDict[name] = otherInfo
    idDict[id] = otherInfo


def all():
    if len(idDict) == 0:
        print("没有学生信息")

    print(idDict)
    for id,info in idDict.items():
        print(F"id: {id} info :{info}")


def get_instruct():
    print_all_option()
    instrct = input()
    if instrct == "1":
        oprAdd()
    elif instrct == "5":
        all()
    elif instrct == "6":
        return
    get_instruct()


if __name__ == '__main__':
    get_instruct()