import os


def fileRead():
    file = open("python1.txt", mode="r",encoding="utf8")
    print(type(file))
    print(file)
    # print(file.readline())
    print("=============")
    # print(file.readlines())
    print("=============")
    print(file.read())


def fileWrite():
    file = open("python1.txt", mode="a", encoding="UTF-8")
    file.write("a")
    file.write("b")
    file.writelines("cccc")
    file.write("""
    我爱北京天安门,
    天安门上太阳升
    """)


def backupFile():
    global path
    path = "python1.txt"
    input = open(path, "r", encoding="utf-8")
    output = open(path.replace(".", "[备份]."), "w", encoding="utf-8")
    while True:
        bytes = input.read(1024)
        if bytes == '':
            break
        output.write(bytes)
    input.close()
    output.close()


if __name__ == '__main__':
    # os.rename(src="python.txt",dst="python2.txt")
    # os.remove("python2.txt")
    fileRead()
    # print(os.cpu_count())
    # print(os.curdir)
    # print(os.listdir)
    # for dir in os.listdir():
    #     print(dir)

