f=open("ch3s.txt","r")
text=str(f.read())
f.close()
f=open("ch3-2.txt","w")
list1=[]
list2=[]
for i in text:
    if i not in list1:
        list1.append(i)
        list2.append(0)
        continue
    index=list1.index(i)
    list2[index]+=1

print(list1,file=f)
print(list2,file=f)
print('\n',file=f)
for v in list2:
    if v==0:
        index=list2.index(v)
        print(list1[index],file=f,end='')
        list1.remove(list1[index])
f.close()

