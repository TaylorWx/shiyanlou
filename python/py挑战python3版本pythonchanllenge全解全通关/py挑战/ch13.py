#coding=gbk
#这里可以不用PIL之Image,直接二进制,多方便
def level_12():
        f=open(r'evil2.gfx','rb') # 注意要二进制方式打开
        data=f.read()
        for i in range(5):
                fo=open(r'%d.gfx'%(i,),'wb') # 二进制写
                fo.write(data[i::5])
                fo.close()
        f.close()

level_12()
