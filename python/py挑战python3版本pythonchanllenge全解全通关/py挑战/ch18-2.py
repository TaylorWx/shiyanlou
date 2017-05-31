#coding=gbk
import urllib.parse
import bz2
import xmlrpc.client
import http.client
f=open('ch18.txt','r')
info=f.read()
f.close()
print(info)
print(type(info))
info=urllib.parse.unquote_to_bytes(info).replace(b'+',b' ',1)
#原来为unquote_plus
#注意这里只需要替换+一次,
info=info[:-2]
print(info)
print(type(info))
#info=b'BZh91AY&SY\x94:\xe2I\x00\x00!\x19\x80P\x81\x11\x00\xafg\x9e\xa0 \x00hE=M\xb5#\xd0\xd4\xd1\xe2\x8d\x06\xa9\xfa&S\xd4\xd3!\xa1\xeai7h\x9b\x9a+\xbf`"\xc5WX\xe1\xadL\x80\xe8V<\xc6\xa8\xdbH&32\x18\xa8x\x01\x08!\x8dS\x0b\xc8\xaf\x96KO\xca2\xb0\xf1\xbd\x1du\xa0\x86\x05\x92s\xb0\x92\xc4Bc\xf1w$S\x85\t\tC\xae$\x90'
print(info)
#a=bz2.compress(b"""is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.""")
#print(a)
info=bz2.decompress(info)
print(info)

# google 得知mozart的老爸叫 Leopold
# 回 13关的电话薄
conn=xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
result=conn.phone('Leopold') # 查Mozart老爸的电话
print (result )# 输出 555-VIOLIN ==> http://www.pythonchallenge.com/pc/return/violin.html
# 提示 no! i mean yes! but ../stuff/violin.php. ==> http://www.pythonchallenge.com/pc/stuff/violin.php
# 显示 it's me. what do you want? 图片是 Leopold的头像？
# 把 the flowers are on their way 这句话放到cookies的info里面发过去试试
h={}
h['cookie']='info='+urllib.parse.quote_plus('the flowers are on their way')
conn=http.client.HTTPConnection('www.pythonchallenge.com')
conn.set_debuglevel(1)
conn.request('GET','http://www.pythonchallenge.com/pc/stuff/violin.php',headers=h)
res=conn.getresponse()
print (res.read())#输出网页中提示
