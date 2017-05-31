import re
f=open("ch4str.txt","r")
text=str(f.read())
f.close()
sDDDsDDDs=re.compile('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
ab=sDDDsDDDs.findall(text)
f=open("ch4.txt","w")
for i in ab:
    zm=i[4]
    print(zm,file=f,end="")
f.close()


