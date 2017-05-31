import os,re,time,zip
ml='ch7channel'
ab=os.listdir(ml)
lenn=len(ab)
link=90052
count=0
sz=re.compile(b'\d+')
ff=open("ch7.txt","w")
while count<lenn:
    try:
        link=ml+"\\"+str(link)+'.txt'
        f=open(link,"rb")
        ab=f.read()
        print(ab,file=ff)
        link=sz.findall(ab)[0]
        f.close()
        link=str(link)[2:-1]
        print(link,file=ff)
    except:
        break



