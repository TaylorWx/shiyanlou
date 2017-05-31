#coding=gbk
import urllib.request,urllib.parse
import xmlrpc.client
import http.client,re,bz2,time
def level_17():
    busynothing='12345'
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s'
    p=re.compile(rb'and the next busynothing is (\d+)',re.M)
    info=''
    while True:
        res=urllib.request.urlopen(url%(busynothing,))
        s=res.info().get('Set-Cookie').split(';',1)[0].split('=')[1]
        #原来为getheaders,现改为get
        print (s)
        info+=s
        data=res.read()
        m=p.search(data)
        if m:
            busynothing=m.group(1)
            busynothing=str(busynothing)[2:-1]
            print ('busynothing=',busynothing)
            time.sleep(0.5)
        else:
            print (data)
            print (info )
            # 输出 BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90
            break

    # BZh打头的看来又需要bz2了

    f=open("ch18.txt","w")
    f.write(info)
    f.close()
    

level_17()
