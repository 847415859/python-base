from datetime import datetime, timedelta


'''
    datetime基本知识点
'''
def datetimeBase():
    '''
        datetime
    '''
    # 1.存储精细度
    now = datetime.now()
    print(datetime.now())
    # 2.计算时间差
    diffValue = datetime(2013, 11, 12, 11, 22, 33, 11) - datetime(2012, 12, 13, 12, 23, 34, 12)
    print(type(diffValue))
    print(f"时间的差值为{diffValue}")
    # 3.加减求另一个时间
    start = datetime(2011, 11, 12)
    print(start + timedelta(30))
    print(start)
    # datetime 数据类型
    # date 年月日
    # time 时分秒 微妙
    print(now.date())
    print(now.time())
    print(now)


if __name__ == '__main__':
    # 1.字符串格式化输出
    datetime = datetime(2022,11,12)
    print(datetime)
    datetimeFomart = datetime.strftime("%Y-%m-%d")
    print(datetimeFomart)

    # 2.字符串转为时间数据类型
    # ① datetime 的 strptime
    print(datetime.strptime("2021-11-23", "%Y-%m-%d"))
    # ② parse