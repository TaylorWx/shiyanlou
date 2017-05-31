f=open("ch3s.txt","r")
text=str(f.read())
f.close()
f=open("ch3.txt","w")
dict={}
for i in text:
    if i not in dict.keys():
        dict[i]=0
        continue
    dict[i]+=1

print(dict,file=f)
print('\n',file=f)
for k,v in dict.items():
    if v==0:
        print(k,file=f,end='')
f.close()

