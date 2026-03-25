try:
    num=int(input("Enter a number"))
    a=[6,3]
    print(a[num])
except ValueError as e:
    print(e)
except IndexError as i:
    print(i)