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
    mandel = ufos.copy() 
    # 直接使用原图的类型、大小和调色板
    mandel.putdata(list(mandelbrot()))
    mandel.show() 
    # 自己画出的图像看上去和给出的图一样
    # 通过比较像素确定自己画的图和给出的图的差异
    differences = [(a - b) for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]
    print (len(differences) )
    # 输出 1679，说明实际上有1679处不同
    print (set(differences) )
    # 输出set([-16, 16])，说明实际上所有差异都是16或者-16
    # 调用level30里面用过的因式分解函数
    print (factor(len(differences)) )
    # 输出 [23, 73] ，说明可以解析为23×73的图像
    # 构造 23×73的图像，放大10倍后显示
    plot=Image.new('L',(23,73))
    plot.putdata([(i < 16) and 255 or 0 for i in differences]) 
    # 是-16则设为255，否则设为0
    plot.resize((230, 730)).show() 
    # 显示一幅奇怪的图像
    # google得知 上面显示的图是由位于美国波多里格的Arecibo天文台的目前全球最大的射电望远镜
    # 发射到外太空以期与外星人沟通的无线电信号。Arecibo天文台的射电望远镜口径350米，就是007《黄金眼》
    # 中出现的那个超大的湖水下的大碗(又想起了里面的漂亮MM ^_^)。
    # 信号含义见 http://zh.wikipedia.org/wiki/%E9%98%BF%E9%9B%B7%E8%A5%BF%E5%8D%9A%E4%BF%A1%E6%81%AF
    # 下一关的key就是 arecibo ==> http://www.pythonchallenge.com/pc/rock/arecibo.html
level_31()
