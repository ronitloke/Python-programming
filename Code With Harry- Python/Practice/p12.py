stuff=["hello",12.65,"hi",75,67,"hey",78,98,True]

# li=[]
# for i in stuff:
#     if isinstance(i,str):
#         li.append(i[::-1])
#     else:
#         li.append(i)
# print(li)

li=[i[::-1] if isinstance(i,str) else i for i in stuff]