li={"apple", "google", "facebook", "microsoft", "pyspiders"}

d={}

for i in li:
    if len(i)%2==0:
        d[i]=len(i)
print(d)