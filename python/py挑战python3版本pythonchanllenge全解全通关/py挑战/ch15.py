#coding=gbk
from PIL import Image,PngImagePlugin

def level_14():
        # 先把wire.png的像素码成100*100
##      my=PIL.Image.new('RGB',(100,100))
##      f=PngImagePlugin.PngImageFile(ur'd:\wire.png')
##      for y in xrange(100):
##              for x in xrange(100):
##                      my.putpixel((x,y), f.getpixel((y*100+x,0)))
##      my.save(ur'd:\14.png','png') 
## 得到的图片里面有红色bit字样 ==> http://www.pythonchallenge.com/pc/return/bit.html
        # 提示 you took the wrong curve.
        # curve是曲线，这么说是要像蛋糕一样把像素盘起来？
        # 提示里面 100*100 = (100+99+99+98) + (...  -->
        # 100*100 图像，从一边开始盘，100->99->99->98正好四条边盘完，再向内侧盘
        # 98->97->97->96 找到规律 x->x-1->x-1->x-2
        # 从左上角顺时针盘
        my=Image.new('RGB',(100,100))
        f=PngImagePlugin.PngImageFile(r'wire.png')
        print ('x,y=%d,%d'%(f.size[0],f.size[1]))
        n=100 # 每条边长度
        x,y=0,0
        i=0
        #采用递增i,来放置pixel
        #螺旋状
        while i<10000:
                #print( 'i,n=%d,%d'%(i,n))
                # 上
                for cnt in range(n):
                        #在指定位置放置指定pixel
                        my.putpixel((x+cnt,y),f.getpixel((i,0)))
                        i+=1

                x+=(n-1)
                # 右
                for cnt in range(1,n):
                        my.putpixel((x,y+cnt),f.getpixel((i,0)))
                        i+=1

                y+=(n-2)
                # 下
                for cnt in range(1,n):
                        my.putpixel((x-cnt,y),f.getpixel((i,0)))
                        i+=1

                x-=(n-2)
                # 左
                for cnt  in range(1,n-1):
                        my.putpixel((x,y-cnt),f.getpixel((i,0)))
                        i+=1
                y-=(n-3)

                n-=2 # 调整要画的边长

        my.save(r'14.png','png') 

level_14()
