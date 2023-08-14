from datetime import date
import os

if __name__ == '__main__':
    # cpu 核心数
    print(os.cpu_count())
    print(os.getpid())
    print(os.name)
    print(os.getcwd())

    print(date.today())
    now = date.today()
    # now.strftime()


    # print(datetime.time)
    # print(datetime.datetime)
    # print(datetime.timedelta)
    # print(datetime.MAXYEAR)
    # print(datetime.MINYEAR)