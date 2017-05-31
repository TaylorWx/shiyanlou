#coding=gbk
import zipfile
f=zipfile.ZipFile(r'21test.zip')
data=f.open(r'package.pack','r',pwd=b'redavni').read()
#注意这里密码要加上个b
open(r'package.pack','wb').write(data)
