#coding=gbk
from PIL import Image
import urllib.request
import wave,os
# ����������Ľⷨ�������
# ����������ر���wave�ļ�
n1 = urllib.request.FancyURLopener()
template = "http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav"
fname=r'level26\25_lake%d.wav'
os.mkdir('level26')
for i in range(1, 26):
    #urllib.request.urlretrieve(template%i,fname%i)
    urlf=n1.open(template%i)#���ƴ��
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

