#coding=gbk
import wave,array
def level_19():
    wi=wave.open(r'indian-2.wav','rb')
 # waveģ����ǰ��δ�õ�
    wo=wave.open(r'indian_inv.wav','wb')
    wo.setparams(wi.getparams())
 # ����ļ����ó��������ļ���ͬ�Ĳ���
    a=array.array('i')
 # arrayģ����ǰ��δ�õ���'i'���������е������������з�������
    a.fromstring(wi.readframes(wi.getnframes()))
 # ������֡��������
    a.byteswap()
 # �ؼ����ⲽ�����������ֽ�
    wo.writeframes(a.tostring())
    wi.close(),wo.close()
 # ��˵���ļ������� you are an idiot ==> http://www.pythonchallenge.com/pc/hex/idiot.html
   
 # "Now you should apologize..."
   
 # ==> http://www.pythonchallenge.com/pc/hex/idiot2.html
   
 # ��֮����ƺ������⣬��Ƶ�ļ�������������ģ�ʵ�����������κ�������ķ���

level_19()
