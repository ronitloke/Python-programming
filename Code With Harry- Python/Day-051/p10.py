word="learning"
with open("practice.txt", "r") as f:
    data=f.read()
    def func1():
        if(data.find(word)) != -1:
            print("found")
        else:
            print("not found")
        return "completed"
    print(func1())

