try:
    a=input()
    if a%2==0:
         print("It is even")
    else:
          print("It is odd")
except:
         print("Invalid input")
finally:
    print("I am always executed")
