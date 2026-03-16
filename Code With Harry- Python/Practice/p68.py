names=["apples","google","persistent","IBM","allas capco","Atos","haber"]

li=[i[::-1] for i in names if(len(i)%2!=0)]
print(li)
