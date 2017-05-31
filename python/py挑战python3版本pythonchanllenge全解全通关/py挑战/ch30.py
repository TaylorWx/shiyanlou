#coding=gbk
import urllib.request,bz2
def level_29():
    n1 = urllib.request.FancyURLopener()
    url='http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'
    lines=n1.open(url).read().splitlines()[12:]
    list=b''
    for line in lines:
        i=len(line)
        item=bytes([i])
        list+=item
        print(item)
    hint=bz2.decompress(list)
    print(hint)

level_29()


