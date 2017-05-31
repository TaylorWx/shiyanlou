#coding=gbk
import zipfile,re
zf=zipfile.ZipFile('channel.zip')
id='90052'
renndigit=re.compile(r"Next nothing is (\d*)")
f=open('ch7-2.txt','w')
while 1:
    text=zf.read("%s.txt" %id).decode('ascii')
    match=renndigit.search(text)
    if match:
        comt=zf.getinfo("%s.txt"%id).comment
        #这里要进行byte-->str,然后str中包括\\n,要替换回来.
        comt=str(comt)[2:-1]
        comt=comt.replace('\\n','\n')
        print(comt,end='',file=f)
        id=match.group(1)
        #原来没用过zipfile,
        #而且正则不大会,因为用其他的去了
    else:
        break
f.close()
zf.close()



