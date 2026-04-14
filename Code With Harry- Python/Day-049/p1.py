#Reading a file

f=open('myfile','r')
#print(f) # output- "<_io.TextIOWrapper name='myfile' mode='r' encoding='cp1252'>"

text=f.read()
print(text)
f.close()