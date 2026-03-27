def func(n1,n2):
    try:
        re=n1/n2
    except ZeroDivisionError:
        print("Error solved")
    else:
        return re
    finally:
        print("It will always execute")
print(func(12,0))