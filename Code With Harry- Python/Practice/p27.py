l=[111,888,999,222,786,136,144]

a=set()
for i in l:
    if (i%100)%2==0:
        a.add(i);
print(a)
