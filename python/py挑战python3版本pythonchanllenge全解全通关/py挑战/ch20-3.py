#coding=gbk
import wave,array
def level_19():
    wi=wave.open(r'indian-2.wav','rb')
 # wave模块以前从未用到
    wo=wave.open(r'indian_inv.wav','wb')
    wo.setparams(wi.getparams())
 # 输出文件设置成与输入文件相同的参数
    a=array.array('i')
 # array模块以前从未用到，'i'代表数组中的数据类型是有符号整型
    a.fromstring(wi.readframes(wi.getnframes()))
 # 将所有帧放入数组
    a.byteswap()
 # 关键是这步，两两交换字节
    wo.writeframes(a.tostring())
    wi.close(),wo.close()
 # 据说新文件能听到 you are an idiot ==> http://www.pythonchallenge.com/pc/hex/idiot.html
   
 # "Now you should apologize..."
   
 # ==> http://www.pythonchallenge.com/pc/hex/idiot2.html
   
 # 总之这关似乎有问题，音频文件听起来乱糟糟的，实在听不出来任何有意义的发音

level_19()
