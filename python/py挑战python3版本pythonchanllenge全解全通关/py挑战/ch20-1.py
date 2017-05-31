#coding=gbk
import urllib.request,urllib.parse
import re,base64
data=open('indian.data','r').read()

def level_19():
    m=re.search(r'--===============1295515792==\n(.*?)--===============1295515792==',data,re.M|re.S)
    m=re.search(r'Content-transfer-encoding: base64\n\n(.*?)\n\n--===============1295515792==',data,re.M|re.S)
    if m:
        s=base64.b64decode(m.group(1))
        open(r'indian.wav','wb').write(s) 
        # 这个文件啥都听不出来 只好翻攻略

level_19()

