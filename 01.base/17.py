
class CustomException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == '__main__':
    try:
        # i = 1 / 0
        i = 1
        raise CustomException("错误了")
    except Exception as ex:
        print("错误了"+ex)
    else:
        print("正常执行")
    finally:
        print("怎么样都能执行")