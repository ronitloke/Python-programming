names=["apple","google","persistent","ibm","atlas capco","atos","haber"]

#li[i if len(i)%2==0 and  for i in names]

li=[]

for i in names:
    if len(i)%2!=0:
        li.append(i[::-1])
    else:
        li.append(i)
print(li)