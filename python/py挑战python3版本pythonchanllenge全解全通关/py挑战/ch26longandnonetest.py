# http://www.pythonchallenge.com/pc/hex/lake.html
# 第25关
# imagine how they sound
# 一个类似puzzle拼图的图片
# 网页注释提示 <!-- can you see the waves? -->
# 脑子转不过来了，看攻略才知道是让你下 http://www.pythonchallenge.com/pc/hex/lake1.wav
# 一直下到5，还有
# 编程实现吧
def level_25():
    # 将25个wave下载
    def part1():
        class myHTTPDefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
            def http_error_default(self, req, fp, code, msg, hdrs):
                if code==404: # 只处理404错误
                    return fp
                raise HTTPError(req.get_full_url(), code, msg, hdrs, fp)
        url='http://www.pythonchallenge.com/pc/hex/lake%d.wav'
        baseurl='http://www.pythonchallenge.com/pc/'
        usr,pwd='butter','fly'
        passman=urllib2.HTTPPasswordMgr() # 密码管理
        passman.add_password('pluses and minuses',baseurl,usr,pwd) # uri 参数不能是变量
        authhandler=urllib2.HTTPBasicAuthHandler(passman) # 基本验证handler
        cj=cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),authhandler,myHTTPDefaultErrorHandler)

        opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) chromeframe/4.0')]
        urllib2.install_opener(opener)
    ##   opener.handle_open['http'][0].set_http_debuglevel(1) # 设置debug以打印出发送和返回的头部信息
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
                print 'done.%d'%(beginidx,) # 可以看到共有25个wave文件，正好和关数一样，也和图片上puzzle拼图的分块数目相同。
                break

    # 至此思路枯竭 找攻略吧。。。
    # 找到一个比较强的攻略：http://garethrees.org/2007/05/07/python-challenge/#level-19
    # 里面说由于用wave editor看波形啥都看不出来,猜想那些不是wave文件
    # 假设是图像文件,由于wave.getnframes()=10800,考虑3字节为1像素,所以有3600像素,
    # 可能是60*60的小图片
    f=wave.open(r'level26\25_lake1.wav')
    print (f.getnframes())
    img=Image.new('RGB',(60,)*2)
    img.fromstring(f.readframes(f.getnframes()))
    img.show() # 能显示，似乎是一张图片的一部分，所以下面尝试将25张图片按5*5方式拼起来

    imgs=[]
    for i in range(1,26): # 将25个wave文件转成25个Image放入imgs
        tmpw=wave.open(r'level25\25_lake%d.wav'%(i,))
        tmpi=Image.new('RGB',(60,)*2)
        tmpi.fromstring(tmpw.readframes(tmpw.getnframes()))
        imgs.append(tmpi)
    img=Image.new('RGB',(300,)*2)
    for i in range(len(imgs)):
        img.paste(imgs[i],( 60*(i%5),60*(i//5))) # 依次将25个image存到一个300×300的大imge中
##   img.show()
    img.save(r'26_lake1.png','png') # 图片显示 decent ==> http://www.pythonchallenge.com/pc/hex/decent.html




