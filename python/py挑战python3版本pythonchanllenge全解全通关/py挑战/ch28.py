#coding=gbk
from PIL import GifImagePlugin,Image
import urllib.request,string,bz2,keyword
def level_27():
    zig=GifImagePlugin.GifImageFile(r'zigzag.gif')
    zigdata=zig.tostring()
    import array
    data=[]
    for i in zigdata[:10]:
        data.append(i)
    data = array.array("B", data).tostring()
    print("zigdata,10:",data[:10])
    
    print (''.join(['%X'%(i,) for i in zigdata[:20]]))
    # 查看前面几个字节，没有头绪)

    #print (len(zig.getcolors()))
    palette=zig.palette.getdata()[1][::3] # 获取其调色板
    data1=[]
    for i in palette[:10]:
        data1.append(i)
    data1 = array.array("B", data1).tostring()
    print("palette,10:",palette[:10])
    #print(data1,type(data1))

    print (''.join(['%X'%(i,) for i in palette[:20]]))

    #t=string.maketrans(''.join([chr(i) for i in range(256)]),palette)
    ch1=b''.join([bytes([i]) for i in range(256)])
    t=bytes.maketrans(ch1,palette)
    zigtrans=zigdata.translate(t) # 用调色板值转换像素值
    print("zigtrans,10",zigtrans[:10])
    print (''.join(['%X'%(i,) for i in zigtrans[:20]]))
    #实现hex(zigtrans[:20],python3下,前面为python2版
    # 还是看不出来什么，不过似乎转换后的数据除了第一个字节外都与原数据很相似)

    print (zigdata[1:]==zigtrans[:-1])
    # 尝试将两组数据中所有不相同的字节放在一起
    deltas=filter(lambda p:p[0]!=p[1],zip(zigdata[1:],zigtrans[:-1]))
    diffs=[b''.join([bytes([p[i]]) for p in deltas]) for i in range(2)]
    print (diffs[0][:20])
    # 看起来是个bz文件)
    print (diffs[1][:20])
    #这一句结果与别人的不同也.

    bz=bz2.BZ2Decompressor().decompress(diffs[0])
    #bz=bz2.decompress(diffs[0])#在python3下要用上面这一句,真是奇怪
    #也许比较的是字节吧
    print (len(bz))
    print (bz[:100])
    # 输出是python的关键字和地址 ../ring/bell.html

    keywords=bz.split(b' ')
    keys={}
    for k in keywords: keys[k]=1
    print (keys.keys())

    print (len(keywords))
    print (len(keys.keys()))
    # 很多关键字
    print (len(keywords)/len(keys.keys()))

    # 将不一样的像素按位置显示出来
    im=Image.new('1',zig.size,0)
    im.putdata([ p[0]==p[1] for p in zip(zigdata[1:],zigtrans[:-1])])
    #im.show() 

    # 有个钥匙图样，左边是not，右边是word，下面是busy?
    # 暗示 not key word
    # 那么找找上面看到的那些关键字里面哪些不是key word
    im.save("27_notkeyword.png","png")

    for k in keys.keys():
        k=str(k)[2:-1]
        if not keyword.iskeyword(k):
            print (k)
            # 打印出来 switch 和 repeat 不是关键字，../ring/bell.html不算。

    # 用switch 和 repeat 分别做用户名和密码,还有print,exec,当然这是python3下的
    k1,k2='switch','repeat'
    t=((k1+":"+k2),(k2+":"+k1))
    n1 = urllib.request.FancyURLopener()
    for i in t:
        try:
            url='http://'+i+'@www.pythonchallenge.com/pc/ring/bell.html'
            r=n1.open(url)
            if r:
                print ('got, %s '%(i))
                # 正确的用户名是repeat 密码是 switch ==> http://www.pythonchallenge.com/pc/ring/bell.html
                break
        except urllib.request.HTTPError:
            pass

level_27()
