import json


def logging(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except Exception as e:
            print(e.__str__())
            with open("err.log","a") as file:
                file.writelines(e.__str__()+"\n")
    return inner

@logging
def err_func():
    1 / 0

err_func()

json.loads()