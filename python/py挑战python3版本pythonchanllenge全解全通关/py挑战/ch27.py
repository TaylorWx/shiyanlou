#coding=gbk
import hashlib,time
def level_26():
    data=open(r'mybroken.zip','rb').read()
    for i in range(len(data)):
        for c in range(256):
            cc=bytes([c])
            newdata=data[:i]+cc+data[i+1:]
            if hashlib.md5(newdata).hexdigest()=='bbb8b499a0eef99b52c7f13f4e78c24b':
                open(r'mybroken_ok.zip','wb').write(newdata) # 修复好的文件打开里面的mybroken.gif, 图中显示 speed
                print ('repaired.')
                return

level_26()
