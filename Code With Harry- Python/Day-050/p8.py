f=open('myfile4','w')
line=['line1','line2','line3']
for l in line:
    f.writelines(l + '\n')
f.close