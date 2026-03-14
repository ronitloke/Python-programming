li=["apple","google","facebook","microsoft","pyspiders"]

d={}
for i in li:
    if(i.startswith("m")):
        d[i]=len(i)
print(d)