count=0
with open("practice1.txt", "r") as f:
    data=f.read()

    num=data.split(",")
    for i in num:
        if(int(i)%2==0):
            count +=1
    print(count)