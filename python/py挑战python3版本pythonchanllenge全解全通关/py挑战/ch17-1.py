#coding=gbk
#˼·�ǽ�����ת��Ϊ640Ϊһ�е����飬
#���ｫ�����ַ���ǰ����b
#������ƥ��ÿ���е�[��һ���ۿ�ǰ][��һ���ۿ�][��һ���ۿ��]�����֣������
#��Ϊ[��һ���ۿ�][��һ���ۿ��][��һ���ۿ�ǰ]
#�����ת����ȥ,��

from PIL import Image
import re
img = Image.open(r"mozart.gif",)
imgtext = img.tostring().replace(b'\n',b'0') 
# ת������Ϊstring�����������ܴ��ڵ�'\n'���滻��
imgtext = b'\n'.join([imgtext[i*640:(i+1)*640] for i in range(480)]) 
# ��640Ϊһ�г�Ϊ480��
imgtext = re.compile(b'^(.*?)(\xc3{5})(.*?)$',re.M).sub(r'\2\3\1', imgtext).replace(b'\n',b'') # ����һ��5���طۿ��Ƶ���ͷ
img.fromstring(imgtext) # ����ش���������
img.save(r"mozartnew.gif")

