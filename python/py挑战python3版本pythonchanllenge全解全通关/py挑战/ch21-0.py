#coding=gbk
import urllib.request,time
n1 = urllib.request.FancyURLopener()
count=0
lists=['30203-31000',\
        '30237-31000',\
        '30284-30294',\
        '30295-30312',\
        '30313-30346',\
        '2123456744-2123456788',\
        '2123456712-2123456743',\
        '1152983631-1153223363']
#注意,这里的'-'不能用' - '等表示,即比较严格 
#至于怎么去找,我也不想去找了,这些列表就这样吧
#要去试探才能得到,我搜索不来

for item in lists:
    n1.addheader('Range','bytes='+item)
    im1 = n1.open('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg')
    #print (im1.info())
    #print(im1.read())
    count+=1
    if count==len(lists):
        open('21test.zip','wb').write(im1.read())
    else:print(im1.read())
    #if count==len(lists)-1 or count==len(lists)-2:
    #    print(im1.read())


