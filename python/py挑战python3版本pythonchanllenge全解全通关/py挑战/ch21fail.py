#coding=gbk
import urllib.request
import http.cookiejar,re
def level_20():
    class myHTTPDefaultErrorHandler(urllib.request.HTTPDefaultErrorHandler):
        def http_error_default(self, req, fp, code, msg, hdrs):
            if code=='416':
                print ('haha')
                return fp
    url='http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    usr,pwd='butter','fly'
##      passman=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman=urllib.request.HTTPPasswordMgr() # �������
    passman.add_password('pluses and minuses',url,usr,pwd)
    authhandler=urllib.request.HTTPBasicAuthHandler(passman) # ������֤handler
    cj=http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),authhandler,myHTTPDefaultErrorHandler)

    opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) chromeframe/4.0')]
    urllib.request.install_opener(opener)
    opener.handle_open['http'][0].set_http_debuglevel(1) 
    # ����debug�Դ�ӡ�����ͺͷ��ص�ͷ����Ϣ
    h={}
    beginidx=1152983631
    #2123456743-10000#30203
    endidx=2123456743
    #beginidx+1000000#30347#beginidx+100
    p=re.compile('bytes \d+-(\d+)/2123456789')
    while True:
        h['Range']='bytes=%d-%d'%(beginidx,endidx)
        req=urllib.request.Request(url,None,headers=h)
        # �˷����Լ�ģ�������֤���������Ƽ���������HTTPPasswordMgr��HTTPBasicAuthHandler����
##      base64string = base64.encodestring('%s:%s' % ('butter','fly'))[:-1]
##      req.add_header("Authorization", "Basic %s" % base64string)
        r = opener.open(req,timeout=15)
        if r:
            res=r.read()
            s=r.info().get('Content-Range')[0]
            m=p.search(s)
            if m: 
                # ����õ���Ч�����ݣ�����
                open(r'unreal.jpg','wb').write(res)
                beginidx=int(m.group(1))+1
                endidx+=10000
                raw_input('next:%d-%d>'%(beginidx,endidx))
                # �õ���Ч���ݺ���ͣһ��
                continue
##          endidx+=1000000
        beginidx+=100
        if beginidx>2123456744:
            print ('done.')
            break

level_20()
