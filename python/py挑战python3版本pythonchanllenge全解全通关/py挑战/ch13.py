#coding=gbk
#������Բ���PIL֮Image,ֱ�Ӷ�����,�෽��
def level_12():
        f=open(r'evil2.gfx','rb') # ע��Ҫ�����Ʒ�ʽ��
        data=f.read()
        for i in range(5):
                fo=open(r'%d.gfx'%(i,),'wb') # ������д
                fo.write(data[i::5])
                fo.close()
        f.close()

level_12()
