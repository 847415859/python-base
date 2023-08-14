
def outer():
    print("outer...")
    def inner():
        print("inner")
    return inner

f = outer()
f()