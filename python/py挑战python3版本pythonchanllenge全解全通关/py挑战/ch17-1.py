#coding=gbk
#思路是将数据转换为640为一行的数组，
#这里将所有字符串前加上b
#用正则匹配每行中的[第一个粉块前][第一个粉块][第一个粉块后]三部分，将其调
#整为[第一个粉块][第一个粉块后][第一个粉块前]
#最后再转换回去,这

from PIL import Image
import re
img = Image.open(r"mozart.gif",)
imgtext = img.tostring().replace(b'\n',b'0') 
# 转换数据为string并将本来可能存在的'\n'先替换掉
imgtext = b'\n'.join([imgtext[i*640:(i+1)*640] for i in range(480)]) 
# 按640为一行成为480行
imgtext = re.compile(b'^(.*?)(\xc3{5})(.*?)$',re.M).sub(r'\2\3\1', imgtext).replace(b'\n',b'') # 将第一个5像素粉块移到开头
img.fromstring(imgtext) # 保存回处理后的数据
img.save(r"mozartnew.gif")

