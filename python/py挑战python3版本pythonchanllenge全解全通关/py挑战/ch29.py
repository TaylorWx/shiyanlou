#coding=gbk
from PIL import PngImagePlugin
def level_28():
    im=PngImagePlugin.PngImageFile(r'bell.png')
    l=[]
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            l.append(im.getpixel((x,y))[1])
    print (l[:10])
    paris=[(l[i],l[i+1]) for i in range(0,len(l),2)] 
    # ����"my paris" ������������Ϊһ��
    
    # ���Կ���������ÿ��paris��������֮�Ϊ42
    print (paris[:10])

    diffs=[abs(i[0]-i[1]) for i in paris] 
    # ������������֮��ľ���ֵ
    print (diffs[:10])

    d=[x for x in diffs if x!=42] 
    # ���˵���ֵ����42��
    print (d)

    s=''.join([chr(x) for x in d]) 
    # ʣ�µĲ�ֵתΪ�ַ�
    print (s )
    # ��� whodunnit().split()[0] ?
    
    # ���˾���Щ��������ˣ�whodunnit�ǵ���β��֪��ıɱ������̽С˵����˼����ô�����뵽Python������Guido Van Rossum ��
    
    # �ѵ��Ƿ����� who done it ˭������Щ
    print ('Guido Van Rossum'.split()[0] )
    # ��� guido ==> http://www.pythonchallenge.com/pc/ring/guido.html

level_28()
