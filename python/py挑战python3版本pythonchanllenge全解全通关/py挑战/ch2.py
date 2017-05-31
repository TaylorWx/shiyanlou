f=open("ch2.txt","w")
str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
def xhzimu2(str):
    for i in str:
        if ord(i)>ord('z') or ord(i)<ord('a'):
            print(i,file=f,end='')
            continue
        if ord(i)>ord('z')-2:
            print(chr(ord(i)-24),file=f,end='')
            continue
        print(chr(ord(i)+2),file=f,end='')
xhzimu2(str)
print('\n',file=f)
xhzimu2('map')
f.close()
