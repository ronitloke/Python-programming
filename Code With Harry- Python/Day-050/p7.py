f=open('myfile3','w')
line=['line1\n','line2\n','line3\n']
f.writelines(line)
f.close

#If we use writelines() function then we can put data line by line in file