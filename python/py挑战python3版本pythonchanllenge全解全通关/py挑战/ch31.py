#coding=gbk
from PIL import Image
import collections,time
    # ����˼·�ǣ���������������(7367)����ʽ�ֽ⣬�õ�53��139
    # Ȼ���Դ���Ϊ��͸ߣ��ø�������256�ĳ˻���Ϊ�Ҷ�ֵ����ͼƬ��
    # ���������õ���ʽ
    # ���ݹ�ʽ�Ը�����3��һ������������ת��Ϊ�ַ����õ���һ�ص����ơ�
def level_30():
    f=open(r'yankeedoodle.csv')
    data=' '.join(f.read().splitlines())
    f.close()
    fields=data.split(', ') 
    newl=[]
    for i in range(len(fields)):
        newl.append(256*float(fields[i]))
    # ע���Ƕ��żӿո����ֻ�ǿո������ƴmessageʱֻ��õ����롣
    print (len(fields))
    n=len(fields) 
    # ��� 7367
    # ��ʽ�ֽ�֮
    def factor(n):
        "Adapted from http://www.math.utah.edu/~carlson/notes/python.pdf"
        d = 2
        factors = []
        while not n % d:
            factors.append(d)
            n /= d
        d = 3
        while n > 1 and d * d <= n:
            if not n % d:
                factors.append(d)
                n /= d
            else:
                d += 2
        if n > 1:
            factors.append(n)
        return factors
    print (factor(n))
    # ��� [53,139]��Ҳ����˵ 53*139=7367
    #
    #   im=Image.new('L',(53,139))
    #
    #   idata=[chr(int(float(x)*256)) for x in fields]
    #
    #   im.fromstring(''.join(idata))
    im=Image.new('L',(53,139))
    #L����ΪP,������ΪF,��Ϊ���ܱ���ͼƬ,�������ҪͼƬ,��Ȼ����,�����im.show
    #����ȡ��ע��
    # 'F'��ʾֱ��ʹ�ø�����
    #im.putdata((map(float,fields),256))
    im.putdata(newl)
    im=im.transpose(Image.FLIP_LEFT_RIGHT) 
    # ���ҷ�ת
    im=im.transpose(Image.ROTATE_90) 
    # ��ת90��
    #im.show() 
    im.save('ch31.png','png')
    # �ܿ�����ʽ n=str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]
    nlist=[]
    for i in range(0,n-2,3):
        n=chr(int(fields[i][5]+fields[i+1][5]+fields[i+2][6]))
        nlist.append(n)
    print (''.join(nlist))
    # ��� So, you found the hidden message.
    # There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.
    # ==>  http://www.pythonchallenge.com/pc/ring/grandpa.html
level_30()
