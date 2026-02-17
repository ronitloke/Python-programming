#<----------Arbitrary arguments----------->

def average(*number): #If we want to add more values of arguments then we need to put a "*" before the args passed in function
    print(type(number))
    sum=0
    for i in number:
        sum=sum+i
        print(sum)
average(5,6,7)

#<----------Keyword Arbitrary arguments---------->
def identity(**name):
    print(type(name))
    print("hello", name["mname"],name["lname"],name["fname"])
identity(fname="ronit",mname="devendra",lname="loke")  #key and value pair