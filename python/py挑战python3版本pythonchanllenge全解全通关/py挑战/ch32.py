#coding=gbk
from PIL import Image
def level_31():
    imgname='mandelbrot.gif'
    ufos = Image.open(imgname)
    def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027,max=128, size=(640, 480)):
        xstep = width / size[0]
        ystep = height / size[1]
        for y in range(size[1] - 1, -1, -1):
            for x in range(size[0]):
                c = complex(left + x * xstep, bottom + y * ystep)
                z = 0+0j
                for i in range(max):
                    z = z * z + c
                    if abs(z) > 2:
                        break
                yield i
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
    mandel = ufos.copy() 
    # ֱ��ʹ��ԭͼ�����͡���С�͵�ɫ��
    mandel.putdata(list(mandelbrot()))
    mandel.show() 
    # �Լ�������ͼ����ȥ�͸�����ͼһ��
    # ͨ���Ƚ�����ȷ���Լ�����ͼ�͸�����ͼ�Ĳ���
    differences = [(a - b) for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]
    print (len(differences) )
    # ��� 1679��˵��ʵ������1679����ͬ
    print (set(differences) )
    # ���set([-16, 16])��˵��ʵ�������в��춼��16����-16
    # ����level30�����ù�����ʽ�ֽ⺯��
    print (factor(len(differences)) )
    # ��� [23, 73] ��˵�����Խ���Ϊ23��73��ͼ��
    # ���� 23��73��ͼ�񣬷Ŵ�10������ʾ
    plot=Image.new('L',(23,73))
    plot.putdata([(i < 16) and 255 or 0 for i in differences]) 
    # ��-16����Ϊ255��������Ϊ0
    plot.resize((230, 730)).show() 
    # ��ʾһ����ֵ�ͼ��
    # google��֪ ������ʾ��ͼ����λ��������������Arecibo����̨��Ŀǰȫ�����������Զ��
    # ���䵽��̫�������������˹�ͨ�����ߵ��źš�Arecibo����̨�������Զ���ھ�350�ף�����007���ƽ��ۡ�
    # �г��ֵ��Ǹ�����ĺ�ˮ�µĴ���(�������������Ư��MM ^_^)��
    # �źź���� http://zh.wikipedia.org/wiki/%E9%98%BF%E9%9B%B7%E8%A5%BF%E5%8D%9A%E4%BF%A1%E6%81%AF
    # ��һ�ص�key���� arecibo ==> http://www.pythonchallenge.com/pc/rock/arecibo.html
level_31()
