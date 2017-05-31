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
    # �鿴ǰ�漸���ֽڣ�û��ͷ��)

    #print (len(zig.getcolors()))
    palette=zig.palette.getdata()[1][::3] # ��ȡ���ɫ��
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
    zigtrans=zigdata.translate(t) # �õ�ɫ��ֵת������ֵ
    print("zigtrans,10",zigtrans[:10])
    print (''.join(['%X'%(i,) for i in zigtrans[:20]]))
    #ʵ��hex(zigtrans[:20],python3��,ǰ��Ϊpython2��
    # ���ǿ�������ʲô�������ƺ�ת��������ݳ��˵�һ���ֽ��ⶼ��ԭ���ݺ�����)

    print (zigdata[1:]==zigtrans[:-1])
    # ���Խ��������������в���ͬ���ֽڷ���һ��
    deltas=filter(lambda p:p[0]!=p[1],zip(zigdata[1:],zigtrans[:-1]))
    diffs=[b''.join([bytes([p[i]]) for p in deltas]) for i in range(2)]
    print (diffs[0][:20])
    # �������Ǹ�bz�ļ�)
    print (diffs[1][:20])
    #��һ��������˵Ĳ�ͬҲ.

    bz=bz2.BZ2Decompressor().decompress(diffs[0])
    #bz=bz2.decompress(diffs[0])#��python3��Ҫ��������һ��,�������
    #Ҳ��Ƚϵ����ֽڰ�
    print (len(bz))
    print (bz[:100])
    # �����python�Ĺؼ��ֺ͵�ַ ../ring/bell.html

    keywords=bz.split(b' ')
    keys={}
    for k in keywords: keys[k]=1
    print (keys.keys())

    print (len(keywords))
    print (len(keys.keys()))
    # �ܶ�ؼ���
    print (len(keywords)/len(keys.keys()))

    # ����һ�������ذ�λ����ʾ����
    im=Image.new('1',zig.size,0)
    im.putdata([ p[0]==p[1] for p in zip(zigdata[1:],zigtrans[:-1])])
    #im.show() 

    # �и�Կ��ͼ���������not���ұ���word��������busy?
    # ��ʾ not key word
    # ��ô�������濴������Щ�ؼ���������Щ����key word
    im.save("27_notkeyword.png","png")

    for k in keys.keys():
        k=str(k)[2:-1]
        if not keyword.iskeyword(k):
            print (k)
            # ��ӡ���� switch �� repeat ���ǹؼ��֣�../ring/bell.html���㡣

    # ��switch �� repeat �ֱ����û���������,����print,exec,��Ȼ����python3�µ�
    k1,k2='switch','repeat'
    t=((k1+":"+k2),(k2+":"+k1))
    n1 = urllib.request.FancyURLopener()
    for i in t:
        try:
            url='http://'+i+'@www.pythonchallenge.com/pc/ring/bell.html'
            r=n1.open(url)
            if r:
                print ('got, %s '%(i))
                # ��ȷ���û�����repeat ������ switch ==> http://www.pythonchallenge.com/pc/ring/bell.html
                break
        except urllib.request.HTTPError:
            pass

level_27()
