#coding=gbk
import zlib,bz2
def level_21():
    # 老外的解法 出处 http://unixwars.com/2007/09/27/python-challenge-level-21-hidden-pack/
    # 思路是先用zlib解，成功则记为' '，失败的话则用bz2解，成功则记为'#'，失败的话则反转数据并复位状态，
    # 如此继续循环，直到上次状态复位后的zlib和bz2尝试都失败则退出
    # 说不清楚还是看程序吧，很诡异。
    st=open(r'package.pack','rb').read()
    log=''
    log_len=len(log)
    while True:
        try: #zlib
            st=zlib.decompress(st)
            log+=' '
        except:
            try: #bzip2
                st=bz2.decompress(st)
                log+='#'
            except: #reverse
                if log_len==len(log): break 
                # 自上次状态复位后的zlib和bz2尝试都失败，则退出
                st=st[::-1] 
                # 反转数据
                print (log[log_len:])
                # 打印上次状态复位后积累的状态字符。 最终输出拼为一个图形字符 显示COPPER ==>  http://www.pythonchallenge.com/pc/hex/copper.html
                log_len=len(log) 
                # 状态复位
    open(r'package.unpack','wb').write(st) 
    # 这个结果文件的内容是“look at your logs” ，提示你打印中间的log信息，也就是程序中的状态字符
    print ('done.')


level_21()
