def fun():
    try:
        a=[3,3,67,8,9]
        i=int(input("Enter index value: "))
        print(a[i])
        return 1
    except:
        print("Invalid input")
        return 0
    finally:
        print("I am always executed")
print(fun())