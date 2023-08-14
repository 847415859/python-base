
max_num = lambda a,b:  a if a > b else b

func1 = lambda n : func1(n -1) + n  if n != 1 else 1

def func2(n):
    if(n == 1):
        return 1
    return  func2(n -1) + n

if __name__ == '__main__':
    print(max_num(1,2))
    print(max_num)

    print((lambda a,b: a if a > b else b)(1,1.5))

    print(func1(100))
    print(func2(100))

    list1 = [{'a': 1}, {'b': 12}, {'c': 10}]

    dict = {"a": 1}
    print(list(dict.values())[0])

    print(list1)
    list1.sort(key= lambda item: list(item.values())[0])
    print(list1)

