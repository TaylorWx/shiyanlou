#coding=gbk
import this,codecs,time
s='va gur snpr bs jung?'
data="".join([this.d.get(c, c) for c in s])
for c in s:
    aa=this.d.get(c,c)
    print(aa,end='')
b=codecs.decode(s, 'rot_13')
print(b)
