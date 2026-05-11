with open('myfile','r') as f:
    f.seek(10) #Skips first 10 bytes
    data=f.read(5) #reads later 5 bytes
print(data)