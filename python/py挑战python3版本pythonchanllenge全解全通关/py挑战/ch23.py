#coding=gbk
from PIL import GifImagePlugin,Image,ImageDraw
import time
def level_22():
    f=GifImagePlugin.GifImageFile(r'white.gif')
    my=Image.new('RGB',(640,480)) # ���ڻ��ַ���ͼƬ
    draw=ImageDraw.Draw(my)
    curpoint=[0,0]
    pointlist=[tuple(curpoint)]
    frameno=1
    while True:
        print ('frame=%d'%(frameno,))
        try:
            for y in range(98,103):#f.size[1]):
                for x in range(98,103):#f.size[0]):
                    if f.getpixel((x,y))!=0:
                        print ('%d: %d,%d=%d'%(frameno,x,y,f.getpixel((x,y))))
        # ��֪ÿ֡���涼�и���ɫ������Ϊ8�ĵ㣬���귶Χ��(98,98)-(102,102)֮��������Ϊż�����൱����3��3�ľŹ�����
                        k='%d-%d'%(x,y)
        # ����Ϊֹû��˼·�ˡ��ο����ԣ�ԭ������ҳ���Ǹ���Ϸҡ�˵�ͼƬ�ǰ�ʾ��Ź���ĵ�����ʸ��������¼�ģ����Ծݴ˻�����������̫���������ˣ�
        #(98,98) (100,98) (102,98)   (-1,-1) (0,-1) (1,-1)
        #(98,100)(100,100)(102,100) == (-1,0) (0,0) (1,0)
        #(98,102)(100,102)(102,102)   (-1,1) (0,1) (1,1)
                        d={ '98-98':(-5,-5),'100-98':(0,-5),'102-98':(5,-5),
                                '98-100':(-5,0),'100-100':(0,0),'102-100':(5,0),
                          '98-102':(-5,5),'100-102':(0,5),'102-102':(5,5)}
                        if d[k]==(0,0):
                            print ('�ص�ԭ��,��ʼ�����ַ�')
                            if len(pointlist)>1:
                                draw.line(pointlist) # �����ַ�
                                del pointlist[:] # ����б�
                                curpoint[0]+=50 # �趨��ʼ���ַ������꣬�������һ���ַ�����
                                curpoint[1]+=50
                                pointlist.append(tuple(curpoint))
                            continue
                        curpoint[0]+=d[k][0]
                        curpoint[1]+=d[k][1]
                        pointlist.append(tuple(curpoint))

            f.seek(f.tell()+1) # ������һ֡
            frameno+=1

        except EOFError as e: # ���һ֡��ᴥ�����쳣
            print ('end of frame.%d'%(frameno,))
            # ��֪��GIF��133֡
            draw.line(pointlist) # �������һ���ַ�
            my.save(r'23_white.png','png') 
            # �ܿ��������ַ�Ϊ bonus ==> http://www.pythonchallenge.com/pc/hex/bonus.html
            break

level_22()
