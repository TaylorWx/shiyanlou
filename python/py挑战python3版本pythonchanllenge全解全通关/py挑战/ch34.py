    #coding=gbk
    # http://www.pythonchallenge.com/pc/rock/beer.html
    # 第33关
    # 33 bottles of beer on the wall
    # 网页注释中提示:
    # <!--
    # If you are blinded by the light,
    # remove its power, with its might.
    # Then from the ashes, fair and square,
    # another truth at you will glare.
    # -->
    #
    # 注意到图像名称是beer1.jpg，看看 http://www.pythonchallenge.com/pc/rock/beer2.jpg
    # 图上提示 no, png，看看 http://www.pythonchallenge.com/pc/rock/beer2.png
    # 好像是个有个x的灰度杂波图
    # 查看图片信息(通过img.getcolors()) 可知，图像有66种颜色:
    # [(1532, 1), (232, 2), (963, 7), (189, 8), (724, 13), (329, 14), (549, 19), (243, 20),
    #  (144, 25), (424, 26), (119, 31), (328, 32), (126, 37), (339, 38), (126, 43), (357, 44),
    #  (107, 49), (225, 50), (79, 55), (609, 56), (181, 61), (356, 62), (70, 67), (298, 68),
    #  (23, 73), (164, 74), (26, 79), (354, 80), (47, 85), (341, 86), (139, 91), (257, 92),
    #  (104, 97), (505, 98), (192, 103), (224, 104), (114, 109), (310, 110), (32, 115), (183, 116),
    #  (238, 121), (198, 122), (117, 127), (327, 128), (110, 133), (342, 134), (118, 139), (342, 140),
    #  (145, 145), (323, 146), (152, 151), (324, 152), (161, 157), (323, 158), (175, 163), (317, 164),
    #  (183, 169), (317, 170), (171, 175), (337, 176), (198, 181), (318, 182), (241, 187), (283, 188),
    #  (1348, 193), (272, 194)
    # 仔细看发现,每两种颜色值相邻，可以分为一组(1和2, 7和8, 13和14 ...)，
    # 每组颜色的像素数累加后开平方可得一个整数，比如颜色1和2的像素数 sqrt(1532+232)=42，
    # 颜色1，2，7和8的像素数 sqrt(1532+232+963+189)=54
    # 颜色1，2，7，8，13和14的像素数 sqrt(1532+232+963+189+724+329)=63
    # 再根据提示中的"light"，"remove its power"和"square" 猜想：
    # 0) 以所有像素为整体开始；
    # 1) 以当前像素数开平方的值做为宽高建立新图片；
    # 2) 将当前像素中颜色值最大的一组像素标为最暗其他则标为最亮(反过来也行)，然后输出到新图片中；
    # 3) 从当前像素中去掉当前颜色值最大的一组(因为最亮嘛)，然后转到第1)步；
    # 如此循环共建立33个新图片，查看一下输出是否有意义
def level_33():
    img=Image.open(r'beer2.png')
    colors=img.getcolors()
    cl=len(colors)
    l=img.getdata() 
    # 当前操作的像素集合
    #
    #    starttime=clock()
    i=cl-1 
    # 65
    while i>0:
        dim=sqrt(len(l)) 
        dim=floor(dim)
        #print(dim,type(dim))
    # 确定宽高
    #
    #        assert dim==dim/1 
    # 可开方为整数
        newimg=Image.new('P',(dim,dim))
        out=[ 255 if x!=colors[i][1] else 0 for x in l] 
    # 亮色赋值为0，其他为255
        newimg.putdata(out)
        newimg.save('level33\\level33_%02d.png'%((cl-i+1)/2,),'png') 
    # 存成33幅图片
    #
    #        newimg.show()
        tmp=[m[1] for m in colors[i-1:i+1]] 
    # 本次操作后需要滤掉的像素值集合
        l=[item for item in l if item not in tmp] 
    # 产生下次需要操作的像素
        i-=2
    #
    #    print ('time=',clock()-starttime)
    # 存成的33幅图片，每个图片上有一个字母分别是：
    # x x x x x      x x x x x
    # x x v i n      e [g] a [r] w
    # i n [e] [m] o  [l] d [i] [n] o
    # [s] l o
    # 其中带[]的表示字母是被方框圈起来的
    # 带[]的字母连起来是 gremlins，查字典是精灵的意思  ==> http://www.pythonchallenge.com/pc/rock/gremlins.html
    # 终于来到了页面 Temporary End!
    # 至此闯关完毕！
    #
if __name__=="__main__":
#    import re
#    #import cookielib
#    import pickle
#    import zipfile
#    from PIL import PngImagePlugin
#    from PIL import JpegImagePlugin
#    from PIL import GifImagePlugin
#    from PIL import ImageDraw
    from PIL import Image
#    import PIL
#    import bz2
#    import calendar
#    import urllib.request
#    #import httplib
#    #import xmlrpclib
#    import gzip
#    import difflib
#    import base64
#    import email
#    import wave
#    import array
#    import zlib
#    import string
    from math import sqrt,floor
#    import hashlib
#    import keyword
#    from io import StringIO
#    from time import clock
    level_33()
