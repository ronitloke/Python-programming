with open('myfile1','w') as f:
    f.write("Hello world")
    f.truncate(5)  # It cut short the content till first 5 bytes
f.close()