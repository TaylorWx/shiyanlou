#coding=gbk
from PIL import Image,PngImagePlugin

def level_14():
        # �Ȱ�wire.png���������100*100
##      my=PIL.Image.new('RGB',(100,100))
##      f=PngImagePlugin.PngImageFile(ur'd:\wire.png')
##      for y in xrange(100):
##              for x in xrange(100):
##                      my.putpixel((x,y), f.getpixel((y*100+x,0)))
##      my.save(ur'd:\14.png','png') 
## �õ���ͼƬ�����к�ɫbit���� ==> http://www.pythonchallenge.com/pc/return/bit.html
        # ��ʾ you took the wrong curve.
        # curve�����ߣ���ô˵��Ҫ�񵰸�һ����������������
        # ��ʾ���� 100*100 = (100+99+99+98) + (...  -->
        # 100*100 ͼ�񣬴�һ�߿�ʼ�̣�100->99->99->98�������������꣬�����ڲ���
        # 98->97->97->96 �ҵ����� x->x-1->x-1->x-2
        # �����Ͻ�˳ʱ����
        my=Image.new('RGB',(100,100))
        f=PngImagePlugin.PngImageFile(r'wire.png')
        print ('x,y=%d,%d'%(f.size[0],f.size[1]))
        n=100 # ÿ���߳���
        x,y=0,0
        i=0
        #���õ���i,������pixel
        #����״
        while i<10000:
                #print( 'i,n=%d,%d'%(i,n))
                # ��
                for cnt in range(n):
                        #��ָ��λ�÷���ָ��pixel
                        my.putpixel((x+cnt,y),f.getpixel((i,0)))
                        i+=1

                x+=(n-1)
                # ��
                for cnt in range(1,n):
                        my.putpixel((x,y+cnt),f.getpixel((i,0)))
                        i+=1

                y+=(n-2)
                # ��
                for cnt in range(1,n):
                        my.putpixel((x-cnt,y),f.getpixel((i,0)))
                        i+=1

                x-=(n-2)
                # ��
                for cnt  in range(1,n-1):
                        my.putpixel((x,y-cnt),f.getpixel((i,0)))
                        i+=1
                y-=(n-3)

                n-=2 # ����Ҫ���ı߳�

        my.save(r'14.png','png') 

level_14()
