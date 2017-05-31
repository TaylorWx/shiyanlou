    #coding=gbk
    # http://www.pythonchallenge.com/pc/rock/beer.html
    # ��33��
    # 33 bottles of beer on the wall
    # ��ҳע������ʾ:
    # <!--
    # If you are blinded by the light,
    # remove its power, with its might.
    # Then from the ashes, fair and square,
    # another truth at you will glare.
    # -->
    #
    # ע�⵽ͼ��������beer1.jpg������ http://www.pythonchallenge.com/pc/rock/beer2.jpg
    # ͼ����ʾ no, png������ http://www.pythonchallenge.com/pc/rock/beer2.png
    # �����Ǹ��и�x�ĻҶ��Ӳ�ͼ
    # �鿴ͼƬ��Ϣ(ͨ��img.getcolors()) ��֪��ͼ����66����ɫ:
    # [(1532, 1), (232, 2), (963, 7), (189, 8), (724, 13), (329, 14), (549, 19), (243, 20),
    #  (144, 25), (424, 26), (119, 31), (328, 32), (126, 37), (339, 38), (126, 43), (357, 44),
    #  (107, 49), (225, 50), (79, 55), (609, 56), (181, 61), (356, 62), (70, 67), (298, 68),
    #  (23, 73), (164, 74), (26, 79), (354, 80), (47, 85), (341, 86), (139, 91), (257, 92),
    #  (104, 97), (505, 98), (192, 103), (224, 104), (114, 109), (310, 110), (32, 115), (183, 116),
    #  (238, 121), (198, 122), (117, 127), (327, 128), (110, 133), (342, 134), (118, 139), (342, 140),
    #  (145, 145), (323, 146), (152, 151), (324, 152), (161, 157), (323, 158), (175, 163), (317, 164),
    #  (183, 169), (317, 170), (171, 175), (337, 176), (198, 181), (318, 182), (241, 187), (283, 188),
    #  (1348, 193), (272, 194)
    # ��ϸ������,ÿ������ɫֵ���ڣ����Է�Ϊһ��(1��2, 7��8, 13��14 ...)��
    # ÿ����ɫ���������ۼӺ�ƽ���ɵ�һ��������������ɫ1��2�������� sqrt(1532+232)=42��
    # ��ɫ1��2��7��8�������� sqrt(1532+232+963+189)=54
    # ��ɫ1��2��7��8��13��14�������� sqrt(1532+232+963+189+724+329)=63
    # �ٸ�����ʾ�е�"light"��"remove its power"��"square" ���룺
    # 0) ����������Ϊ���忪ʼ��
    # 1) �Ե�ǰ��������ƽ����ֵ��Ϊ��߽�����ͼƬ��
    # 2) ����ǰ��������ɫֵ����һ�����ر�Ϊ��������Ϊ����(������Ҳ��)��Ȼ���������ͼƬ�У�
    # 3) �ӵ�ǰ������ȥ����ǰ��ɫֵ����һ��(��Ϊ������)��Ȼ��ת����1)����
    # ���ѭ��������33����ͼƬ���鿴һ������Ƿ�������
def level_33():
    img=Image.open(r'beer2.png')
    colors=img.getcolors()
    cl=len(colors)
    l=img.getdata() 
    # ��ǰ���������ؼ���
    #
    #    starttime=clock()
    i=cl-1 
    # 65
    while i>0:
        dim=sqrt(len(l)) 
        dim=floor(dim)
        #print(dim,type(dim))
    # ȷ�����
    #
    #        assert dim==dim/1 
    # �ɿ���Ϊ����
        newimg=Image.new('P',(dim,dim))
        out=[ 255 if x!=colors[i][1] else 0 for x in l] 
    # ��ɫ��ֵΪ0������Ϊ255
        newimg.putdata(out)
        newimg.save('level33\\level33_%02d.png'%((cl-i+1)/2,),'png') 
    # ���33��ͼƬ
    #
    #        newimg.show()
        tmp=[m[1] for m in colors[i-1:i+1]] 
    # ���β�������Ҫ�˵�������ֵ����
        l=[item for item in l if item not in tmp] 
    # �����´���Ҫ����������
        i-=2
    #
    #    print ('time=',clock()-starttime)
    # ��ɵ�33��ͼƬ��ÿ��ͼƬ����һ����ĸ�ֱ��ǣ�
    # x x x x x      x x x x x
    # x x v i n      e [g] a [r] w
    # i n [e] [m] o  [l] d [i] [n] o
    # [s] l o
    # ���д�[]�ı�ʾ��ĸ�Ǳ�����Ȧ������
    # ��[]����ĸ�������� gremlins�����ֵ��Ǿ������˼  ==> http://www.pythonchallenge.com/pc/rock/gremlins.html
    # ����������ҳ�� Temporary End!
    # ���˴�����ϣ�
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
