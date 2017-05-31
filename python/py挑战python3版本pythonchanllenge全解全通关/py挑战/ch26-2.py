#coding=gbk
from PIL import Image
import urllib.request
import wave,os
# 下面是老外的解法，更简洁
# 四行完成下载保存wave文件
n1 = urllib.request.FancyURLopener()
template = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
fname=r'level26\25_lake%d.wav'
os.mkdir('level26')
for i in range(1, 26):
    #urllib.request.urlretrieve(template%i,fname%i)
    urlf=n1.open(template%i)#完成拼接
    open(fname%i,'wb').write(urlf.read())
l=[]
for i in range(1,26):
    f=wave.open(r'25_lake%d.wav'%i,'rb')
    l.append(f.readframes(f.getnframes()))
    f.close()
im=Image.new('RGB',(300,300))
for i in range(25):
    im.paste(Image.fromstring('RGB',(60,60),l[i]),( 60*(i%5),60*(i//5)))
im.save(r'26_lake2.png','png')

