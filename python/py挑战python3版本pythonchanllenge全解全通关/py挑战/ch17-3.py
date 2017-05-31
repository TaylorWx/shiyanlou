#coding=gbk
from PIL import GifImagePlugin,Image
def level_16():
##      # 尝试把不是粉短线的颜色都去掉
##      f=GifImagePlugin.GifImageFile(ur'd:\mozart.gif')
##      mf=PIL.Image.new('P',f.size)
##      for y in range(f.size[1]):
##              for x in range(f.size[0]):
##                      if f.getpixel((x,y))==195:
##                              mf.putpixel((x,y),195)
##      mf.save(ur'd:\16.gif','gif') # 啥都看不出来 查看攻略 原来所谓get this straight是说把这些粉短线都按行对齐

        f=GifImagePlugin.GifImageFile(r'mozart.gif')
        mf=Image.new('P',f.size)
        mf.putpalette(f.getpalette()) 
        # 用原图的调色板
        for y in range(f.size[1]):
                for x in range(f.size[0]):
                        if f.getpixel((x,y))==195: 
                            # 找到头一个粉色像素 以此为对准线
                                for mx in range(f.size[0]):
                                        mf.putpixel((mx,y),f.getpixel(((mx+x)%f.size[0],y))) 
                                        #往前走mx<--mx+x之前替换
                                        # 将从这个粉色像素开始的一行复制到新图片中
                                break
        mf.save(r'mozart16.gif','gif') 
        # 图像中包含romance ==> http://www.pythonchallenge.com/pc/return/romance.html



level_16()
