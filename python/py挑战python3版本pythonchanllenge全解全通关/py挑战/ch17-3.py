#coding=gbk
from PIL import GifImagePlugin,Image
def level_16():
##      # ���԰Ѳ��Ƿ۶��ߵ���ɫ��ȥ��
##      f=GifImagePlugin.GifImageFile(ur'd:\mozart.gif')
##      mf=PIL.Image.new('P',f.size)
##      for y in range(f.size[1]):
##              for x in range(f.size[0]):
##                      if f.getpixel((x,y))==195:
##                              mf.putpixel((x,y),195)
##      mf.save(ur'd:\16.gif','gif') # ɶ���������� �鿴���� ԭ����νget this straight��˵����Щ�۶��߶����ж���

        f=GifImagePlugin.GifImageFile(r'mozart.gif')
        mf=Image.new('P',f.size)
        mf.putpalette(f.getpalette()) 
        # ��ԭͼ�ĵ�ɫ��
        for y in range(f.size[1]):
                for x in range(f.size[0]):
                        if f.getpixel((x,y))==195: 
                            # �ҵ�ͷһ����ɫ���� �Դ�Ϊ��׼��
                                for mx in range(f.size[0]):
                                        mf.putpixel((mx,y),f.getpixel(((mx+x)%f.size[0],y))) 
                                        #��ǰ��mx<--mx+x֮ǰ�滻
                                        # ���������ɫ���ؿ�ʼ��һ�и��Ƶ���ͼƬ��
                                break
        mf.save(r'mozart16.gif','gif') 
        # ͼ���а���romance ==> http://www.pythonchallenge.com/pc/return/romance.html



level_16()
