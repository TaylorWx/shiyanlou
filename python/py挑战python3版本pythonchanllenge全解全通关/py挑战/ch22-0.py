#coding=gbk
import zipfile
f=zipfile.ZipFile(r'21test.zip')
data=f.open(r'package.pack','r',pwd=b'redavni').read()
#ע����������Ҫ���ϸ�b
open(r'package.pack','wb').write(data)
