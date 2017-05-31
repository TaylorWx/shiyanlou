#coding=gbk
from PIL import GifImagePlugin,Image,ImageDraw
import time
def level_22():
    f=GifImagePlugin.GifImageFile(r'white.gif')
    my=Image.new('RGB',(640,480)) # 用于画字符的图片
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
        # 可知每帧里面都有个调色板索引为8的点，坐标范围在(98,98)-(102,102)之间且坐标为偶数，相当于在3×3的九宫格中
                        k='%d-%d'%(x,y)
        # 到此为止没有思路了。参考攻略，原来是网页上那个游戏摇杆的图片是暗示你九宫格的点是用矢量方法记录的，可以据此划出线条来，太有想象力了！
        #(98,98) (100,98) (102,98)   (-1,-1) (0,-1) (1,-1)
        #(98,100)(100,100)(102,100) == (-1,0) (0,0) (1,0)
        #(98,102)(100,102)(102,102)   (-1,1) (0,1) (1,1)
                        d={ '98-98':(-5,-5),'100-98':(0,-5),'102-98':(5,-5),
                                '98-100':(-5,0),'100-100':(0,0),'102-100':(5,0),
                          '98-102':(-5,5),'100-102':(0,5),'102-102':(5,5)}
                        if d[k]==(0,0):
                            print ('回到原点,开始画新字符')
                            if len(pointlist)>1:
                                draw.line(pointlist) # 画出字符
                                del pointlist[:] # 清空列表
                                curpoint[0]+=50 # 设定开始画字符的坐标，以免把上一个字符覆盖
                                curpoint[1]+=50
                                pointlist.append(tuple(curpoint))
                            continue
                        curpoint[0]+=d[k][0]
                        curpoint[1]+=d[k][1]
                        pointlist.append(tuple(curpoint))

            f.seek(f.tell()+1) # 跳到下一帧
            frameno+=1

        except EOFError as e: # 最后一帧后会触发此异常
            print ('end of frame.%d'%(frameno,))
            # 可知此GIF有133帧
            draw.line(pointlist) # 画出最后一个字符
            my.save(r'23_white.png','png') 
            # 能看出画的字符为 bonus ==> http://www.pythonchallenge.com/pc/hex/bonus.html
            break

level_22()
