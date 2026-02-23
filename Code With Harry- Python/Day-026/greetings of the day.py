import time

print("Greetings of the day")

x=time.strftime("&H:&M:&S")

if x>"04:00:00" and x<"12:00:00":
    print("Good morning")
elif x>"12:00:00" and x<"16:00:00":
    print("Good afternoon")
elif x>"16:00:00" and x<"21:00:00":
    print("Good evening")
else:
    print("Good night")