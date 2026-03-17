names=["apples","google","persistent","IBM","allas capco","Atos","haber"]

li=[i[::-1] if(len(i)%2!=0) else i for i in names]
print(li)
