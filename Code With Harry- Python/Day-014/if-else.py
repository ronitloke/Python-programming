a=int(input("Enter your age: "))
print("The age is",a)
b=int(input("Enter the weight: "))
print("The weight is",b)


if(a>=18):
    if(b>=50):
        print("The person is eligible to vote")
    else:
        print("The person is not meeting all requirements to vote")
elif(a<=18):
    if(b<=50):
        print("The person is not eligible to vote")
    else:
        print("The person is not at all meeting any requirements to vote")
else:
    print("Please enter a valid input")
