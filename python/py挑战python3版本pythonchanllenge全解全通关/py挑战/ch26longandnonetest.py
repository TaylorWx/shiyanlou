# http://www.pythonchallenge.com/pc/hex/lake.html
# ��25��
# imagine how they sound
# һ������puzzleƴͼ��ͼƬ
# ��ҳע����ʾ <!-- can you see the waves? -->
# ����ת�������ˣ������Բ�֪���������� http://www.pythonchallenge.com/pc/hex/lake1.wav
# һֱ�µ�5������
# ���ʵ�ְ�
def level_25():
    # ��25��wave����
    def part1():
        class myHTTPDefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
            def http_error_default(self, req, fp, code, msg, hdrs):
                if code==404: # ֻ����404����
                    return fp
                raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
        url='http://www.pythonchallenge.com/pc/hex/lake%d.wav'
        baseurl='http://www.pythonchallenge.com/pc/'
        usr,pwd='butter','fly'
        passman=urllib2.HTTPPasswordMgr() # �������
        passman.add_password('pluses and minuses',baseurl,usr,pwd) # uri ���������Ǳ���
        authhandler=urllib2.HTTPBasicAuthHandler(passman) # ������֤handler
        cj=cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),authhandler,myHTTPDefaultErrorHandler)

        opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) chromeframe/4.0')]
        urllib2.install_opener(opener)
    ##   opener.handle_open['http'][0].set_http_debuglevel(1) # ����debug�Դ�ӡ�����ͺͷ��ص�ͷ����Ϣ
        h={}
        beginidx=1
        while True:
            req=urllib2.Request(url%(beginidx,),None,headers=h)
            r = opener.open(req,timeout=10)
    ##       print '%d=%d'%(beginidx,r.code)
            if r and r.code!=404:
                res=r.read()
                open(r'level26\25_lake%d.wav'%(beginidx,),'wb').write(res)
                beginidx+=1
            else:
                print 'done.%d'%(beginidx,) # ���Կ�������25��wave�ļ������ú͹���һ����Ҳ��ͼƬ��puzzleƴͼ�ķֿ���Ŀ��ͬ��
                break

    # ����˼·�ݽ� �ҹ��԰ɡ�����
    # �ҵ�һ���Ƚ�ǿ�Ĺ��ԣ�http://garethrees.org/2007/05/07/python-challenge/#level-19
    # ����˵������wave editor������ɶ����������,������Щ����wave�ļ�
    # ������ͼ���ļ�,����wave.getnframes()=10800,����3�ֽ�Ϊ1����,������3600����,
    # ������60*60��СͼƬ
    f=wave.open(r'level26\25_lake1.wav')
    print (f.getnframes())
    img=Image.new('RGB',(60,)*2)
    img.fromstring(f.readframes(f.getnframes()))
    img.show() # ����ʾ���ƺ���һ��ͼƬ��һ���֣��������波�Խ�25��ͼƬ��5*5��ʽƴ����

    imgs=[]
    for i in range(1,26): # ��25��wave�ļ�ת��25��Image����imgs
        tmpw=wave.open(r'level25\25_lake%d.wav'%(i,))
        tmpi=Image.new('RGB',(60,)*2)
        tmpi.fromstring(tmpw.readframes(tmpw.getnframes()))
        imgs.append(tmpi)
    img=Image.new('RGB',(300,)*2)
    for i in range(len(imgs)):
        img.paste(imgs[i],( 60*(i%5),60*(i//5))) # ���ν�25��image�浽һ��300��300�Ĵ�imge��
##   img.show()
    img.save(r'26_lake1.png','png') # ͼƬ��ʾ decent ==> http://www.pythonchallenge.com/pc/hex/decent.html




