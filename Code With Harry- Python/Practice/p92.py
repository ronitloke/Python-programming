def add(a,b):
    try:
        fc= a+b
    except BaseException:
        print("Exception solved")
    else:
        return fc
    finally:
        print("It will always execute")
print(add(10,"20"))