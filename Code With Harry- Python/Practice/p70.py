li=["hello",12.65,"hi",75,67,"hey",78,98,True]

a=[i[::-1] if(isinstance(i,str)) else i for i in li]
print(a)