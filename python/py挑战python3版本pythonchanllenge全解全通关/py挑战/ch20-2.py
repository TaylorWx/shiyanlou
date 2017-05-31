#coding=gbk
import re,email,time
data=open('indian.data','r').read()
m=re.search(r'<!--\n(.*?)-->',data,re.M|re.S)
mail=email.message_from_string(m.group(1)) # email模块以前从未用到
for part in mail.walk():
    if part.get_content_maintype()=='audio':
        audio=part.get_payload(decode=1)
        open(r'indian-2.wav','wb').write(audio) 

