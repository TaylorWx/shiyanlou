#coding=gbk
from PIL import Image
import collections,time
    # 基本思路是：将浮点数的总数(7367)做因式分解，得到53和139
    # 然后以此做为宽和高，用浮点数与256的乘积作为灰度值画成图片，
    # 调整方向后得到公式
    # 根据公式对浮点数3个一组操作，将结果转换为字符，得到下一关的名称。
def level_30():
    f=open(r'yankeedoodle.csv')
    data=' '.join(f.read().splitlines())
    f.close()
    fields=data.split(', ') 
    newl=[]
    for i in range(len(fields)):
        newl.append(256*float(fields[i]))
    # 注意是逗号加空格！如果只是空格，则后面拼message时只会得到乱码。
    print (len(fields))
    n=len(fields) 
    # 输出 7367
    # 因式分解之
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
    # 输出 [53,139]，也就是说 53*139=7367
    #
    #   im=Image.new('L',(53,139))
    #
    #   idata=[chr(int(float(x)*256)) for x in fields]
    #
    #   im.fromstring(''.join(idata))
    im=Image.new('L',(53,139))
    #L可以为P,但不能为F,因为不能保存图片,如果不需要图片,当然可以,下面的im.show
    #可以取消注释
    # 'F'表示直接使用浮点数
    #im.putdata((map(float,fields),256))
    im.putdata(newl)
    im=im.transpose(Image.FLIP_LEFT_RIGHT) 
    # 左右翻转
    im=im.transpose(Image.ROTATE_90) 
    # 旋转90度
    #im.show() 
    im.save('ch31.png','png')
    # 能看到公式 n=str(x[i])[5]+str(x[i+1])[5]+str(x[i+2])[6]
    nlist=[]
    for i in range(0,n-2,3):
        n=chr(int(fields[i][5]+fields[i+1][5]+fields[i+2][6]))
        nlist.append(n)
    print (''.join(nlist))
    # 输出 So, you found the hidden message.
    # There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.
    # ==>  http://www.pythonchallenge.com/pc/ring/grandpa.html
level_30()
