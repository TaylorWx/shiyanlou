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
        #����Ҫ����byte-->str,Ȼ��str�а���\\n,Ҫ�滻����.
        comt=str(comt)[2:-1]
        comt=comt.replace('\\n','\n')
        print(comt,end='',file=f)
        id=match.group(1)
        #ԭ��û�ù�zipfile,
        #�������򲻴��,��Ϊ��������ȥ��
    else:
        break
f.close()
zf.close()



