names=["apple","google","persistent","ibm","atlas capco","atos","haber"]

# d={}
#
# for i in names:
#     d[i]=len(i)
# print(d)

d={i:len(i) for i in names}
print(d)