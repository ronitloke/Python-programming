with open('myfile1','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        m1=int(line.split(",")[0])
        m2=int(line.split(",")[1])
        m3=int(line.split(",")[2])
        print(f"Student 1 marks in maths is :{m1}")
        print(f"Student 2 marks in english is :{m2}")
        print(f"Student 3 marks in science is :{m3}")
    print(line)

