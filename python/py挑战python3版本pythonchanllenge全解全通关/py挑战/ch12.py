#coding=gbk
from PIL import Image  
  
im = Image.open("cave.jpg")  
w, h = im.size  
o = e = Image.new(im.mode, (w//2, h//2))
#���ڱ�����������ͼ��������ͼ, ��СΪԭͼ��һ��  
for x in range(w):  
    for y in range(h):  
        if (x + y * w)%2:
            #�ж������������ż  
            o.putpixel((x//2,y//2), im.getpixel((x,y)))  
        else:  
            e.putpixel((x//2,y//2), im.getpixel((x,y)))  
o.show()  
e.show()  

