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
    # 根据"my paris" 将像素两两分为一组
    
    # 可以看出基本上每个paris内两像素之差都为42
    print (paris[:10])

    diffs=[abs(i[0]-i[1]) for i in paris] 
    # 计算两两像素之差的绝对值
    print (diffs[:10])

    d=[x for x in diffs if x!=42] 
    # 过滤掉差值等于42的
    print (d)

    s=''.join([chr(x) for x in d]) 
    # 剩下的差值转为字符
    print (s )
    # 输出 whodunnit().split()[0] ?
    
    # 到此就有些让我奇怪了，whodunnit是到结尾才知道谋杀犯的侦探小说的意思，怎么会联想到Python发明人Guido Van Rossum ？
    
    # 难道是发音像 who done it 谁做了这些
    print ('Guido Van Rossum'.split()[0] )
    # 输出 guido ==> http://www.pythonchallenge.com/pc/ring/guido.html

level_28()
