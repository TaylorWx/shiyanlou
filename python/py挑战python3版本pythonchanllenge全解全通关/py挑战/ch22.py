#coding=gbk
import zlib,bz2
def level_21():
    # ����Ľⷨ ���� http://unixwars.com/2007/09/27/python-challenge-level-21-hidden-pack/
    # ˼·������zlib�⣬�ɹ����Ϊ' '��ʧ�ܵĻ�����bz2�⣬�ɹ����Ϊ'#'��ʧ�ܵĻ���ת���ݲ���λ״̬��
    # ��˼���ѭ����ֱ���ϴ�״̬��λ���zlib��bz2���Զ�ʧ�����˳�
    # ˵��������ǿ�����ɣ��ܹ��졣
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
                # ���ϴ�״̬��λ���zlib��bz2���Զ�ʧ�ܣ����˳�
                st=st[::-1] 
                # ��ת����
                print (log[log_len:])
                # ��ӡ�ϴ�״̬��λ����۵�״̬�ַ��� �������ƴΪһ��ͼ���ַ� ��ʾCOPPER ==>  http://www.pythonchallenge.com/pc/hex/copper.html
                log_len=len(log) 
                # ״̬��λ
    open(r'package.unpack','wb').write(st) 
    # �������ļ��������ǡ�look at your logs�� ����ʾ���ӡ�м��log��Ϣ��Ҳ���ǳ����е�״̬�ַ�
    print ('done.')


level_21()
