import time

print("Greetings for the day")

x=time.strftime('%H:%M:%S')
print(x)

if(x<"12:00:00"):
    print("Hello sir! Good Morning")
    
elif(x>"12:00:00" and x<"16:00:00"):
    print("Hello sir! Good Afternoon")
    
elif(x>"16:00:00" and x<"22:00:00"):
    print("Hello sir! Good Evening")
else:
    print("Good night")
