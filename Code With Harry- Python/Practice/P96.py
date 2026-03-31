a=(int(input("Enter any num: ")))

try:
    if(a=="quit"):
        print(a)
except Exception as e:
    print(e)
else:
    raise Exception("invalid")

