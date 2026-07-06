with open("practice1.txt", "r") as f:
    data=f.read()
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
