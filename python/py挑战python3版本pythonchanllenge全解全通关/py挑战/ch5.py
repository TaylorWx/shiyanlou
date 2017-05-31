import urllib.request
import re,time
ab='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
a='63579'
count=0
digit=re.compile(b'\d+')
while count<410:
    url=ab+a
    print(url)
    urlf=urllib.request.urlopen(url)
    text=urlf.read()
    print(text)
    a=digit.findall(text)
    a=str(a[0])[2:-1]
    print(a)
    count+=1
f.close()
