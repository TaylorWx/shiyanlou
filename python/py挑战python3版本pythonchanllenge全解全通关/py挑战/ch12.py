#coding=gbk
from PIL import Image  
  
im = Image.open("cave.jpg")  
w, h = im.size  
o = e = Image.new(im.mode, (w//2, h//2))
#用于保存分离出来的图的两个空图, 大小为原图的一半  
for x in range(w):  
    for y in range(h):  
        if (x + y * w)%2:
            #判断像素坐标的奇偶  
            o.putpixel((x//2,y//2), im.getpixel((x,y)))  
        else:  
            e.putpixel((x//2,y//2), im.getpixel((x,y)))  
o.show()  
e.show()  

