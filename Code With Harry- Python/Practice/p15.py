d={"a":1,"b":2,"c":3,"d":4}

# d1={}
# for key,value in d.items():
#     d1[value]=key
# print(d1)

d1={value:key for key,value in d.items()}
print(d1)