prices={"IBM":678.9,"persistent":515.8,"sony":200.8,"microland":313.7,"gajshield":400.8}

# d={}
#
# for key,value in prices.items():
#     if value >= 300:
#         d[key]=value
# print(d)

d={key:value for key,value in prices.items() if value>=300}
print(d)