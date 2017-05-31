#coding=gbk
from PIL import Image,PngImagePlugin
def level15():
      my=Image.new('RGB',(100,100))
      f=PngImagePlugin.PngImageFile(r'wire.png')
      for y in range(100):
              for x in range(100):
                      my.putpixel((x,y), f.getpixel((y*100+x,0)))
      my.save(r'15.png','png') 
      # 得到的图片里面有红色bit字样 ==> http://www.pythonchallenge.com/pc/return/bit.html
level15()
