#coding=gbk
import gzip,difflib,time
import urllib.parse
from PIL import Image
def level_18():
    data=gzip.GzipFile(r'deltas.gz').read() # ��gz�ļ���ȡ����
    data=data.splitlines() # ת��Ϊ�ַ����б�
    left,right,png=[],[],['','','']
    for line in data:
        left.append(str(line[:53])) # ������벿��
        right.append(str(line[56:])) # �����Ұ벿��
    diff=list(difflib.ndiff(left,right)) 
    # �ؼ������ ����ndiff�Ƚ������ַ����б����ص�ÿ�п�ͷΪ'- '��'+ '��'  'ָʾ�����Ƕ����Ψһ���Ƕ��ұ�Ψһ�������߶�����

    for line in diff:
        line=line[4:-1]
        bytes=[chr(int(byte,16)) for byte in line[2:].split()] # ת������

        if line[0]=='-': 
            png[0]+=''.join(bytes) 
        # '- ' line unique to sequence 1
        elif line[0]=='+': png[1]+=''.join(bytes) 
        # '+ ' line unique to sequence 2
        elif line[0]==' ': png[2]+=''.join(bytes) 

        # '  ' line common to both sequences


    for i in range(3):
        open(r'18_%d.png'%i,'w').write(png[i]) 
        # 18_0.png: ��ʾfly    18_1.png: ��ʾbutter    18_2.png: ��ʾ../hex/bin.html
        # ==> http://www.pythonchallenge.com/pc/hex/bin.html �û��� butter ���� fly (��ʾ��ָʾ "pluses and minuses" �� + -)


level_18()
