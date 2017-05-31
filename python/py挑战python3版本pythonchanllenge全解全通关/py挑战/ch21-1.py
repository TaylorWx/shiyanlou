#coding=gbk
import urllib.request
import re
def fencebreaking():
    auth = urllib.request.HTTPBasicAuthHandler()
    auth.add_password('pluses and minuses', 'www.pythonchallenge.com',
        'butter', 'fly')
    urllib.request.install_opener(urllib.request.build_opener(auth))
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    range = re.compile('bytes (\d+)-(\d+)/(\d+)').search
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    start, end, length = [int(i) \
            for i in range(resp.info()['content-range']).groups()]
    req.add_header('Range', '')
    while end:
        try:
            req.headers['Range'] = 'bytes=%i-' % (end + 1)
            resp = urllib.request.urlopen(req)
            print (resp.read())
            start, end, length = [int(i) \
                for i in range(resp.info()['content-range']).groups()]
        except:
            break
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    req = urllib.request.Request(url, headers={'Range': 'bytes=2123456789-'})
    resp = urllib.request.urlopen(req)
    print (resp.read())
    print (resp.info())
    req.headers['Range'] = 'bytes=2123456743-'
    resp = urllib.request.urlopen(req)
    print (resp.read())
    req.headers['Range'] = 'bytes=1152983631-'
    resp = urllib.request.urlopen(req)
    print(resp.info())
    #print (resp.read())
    open('21test.zip','wb').write(resp.read())

fencebreaking()
