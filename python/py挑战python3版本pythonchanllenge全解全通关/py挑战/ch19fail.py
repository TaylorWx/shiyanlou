#coding=gbk
import gzip,difflib,time
import urllib.parse
from PIL import Image
def level_18():
    data=gzip.GzipFile(r'deltas.gz').read() # 打开gz文件读取数据
    data=data.splitlines() # 转换为字符串列表
    left,right,png=[],[],['','','']
    for line in data:
        left.append(str(line[:53])) # 保存左半部份
        right.append(str(line[56:])) # 保存右半部分
    diff=list(difflib.ndiff(left,right)) 
    # 关键是这句 调用ndiff比较两个字符串列表，返回的每行开头为'- '或'+ '或'  '指示本行是对左边唯一还是对右边唯一还是两边都包含

    for line in diff:
        line=line[4:-1]
        bytes=[chr(int(byte,16)) for byte in line[2:].split()] # 转换编码

        if line[0]=='-': 
            png[0]+=''.join(bytes) 
        # '- ' line unique to sequence 1
        elif line[0]=='+': png[1]+=''.join(bytes) 
        # '+ ' line unique to sequence 2
        elif line[0]==' ': png[2]+=''.join(bytes) 

        # '  ' line common to both sequences


    for i in range(3):
        open(r'18_%d.png'%i,'w').write(png[i]) 
        # 18_0.png: 显示fly    18_1.png: 显示butter    18_2.png: 显示../hex/bin.html
        # ==> http://www.pythonchallenge.com/pc/hex/bin.html 用户名 butter 密码 fly (提示框指示 "pluses and minuses" 即 + -)


level_18()
