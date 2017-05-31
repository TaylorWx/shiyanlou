import pickle,urllib.request,sys
#coding=gbk
#channel看不清
urlf=urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
pickledata=urlf.read()
entry = pickle.loads(pickledata)
f=open('ch6.txt','w')
for line in entry:
    for elem in line:
        print(elem[0]*elem[1],end='',file=f)
    print('\n',file=f)
f.close()
