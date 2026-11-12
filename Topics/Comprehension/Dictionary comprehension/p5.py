dial_codes=[(91,"India"),(1,"America"),(86,"china"),(55,"brazil"),(7,"Russia")]
d={}
for i,j in dial_codes:
    d[i]=j
print(d)

d={i:j for i,j in dial_codes}
print(d)