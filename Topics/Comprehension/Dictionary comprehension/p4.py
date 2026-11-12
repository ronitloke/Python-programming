prices={"ibm":678.9,"persistent":515.8,"sony":200.8,"microland":313.7,"gajshield":400.8}
#without dict comp
d={}
for i,j in prices.items():
    if j>300:
        d[j]=i
    else:
        d[i]=j
print(d)



#with dict comp
#d={j:i if(j>300) else i:j for i,j in prices.items()}
#print(d)