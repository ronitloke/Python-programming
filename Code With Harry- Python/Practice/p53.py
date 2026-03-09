num=int(input())
if(num%7==0 and num%5==0):
    print("num is divisible by 7 and 5")
elif(num%7==0):
    print("num is divisible by 7")
elif(num%5==0):
    print("num is divisible by 5")
else:
    print("non divisible by both")
