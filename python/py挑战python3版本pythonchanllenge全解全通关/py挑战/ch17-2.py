#coding=gbk
from PIL import Image,ImageChops
im = Image.open(r"mozart.gif")
magic = bytes([195])#ԭ��ֻ��Ҫ��chr(195)-->bytes�ͺ�
for y in range(im.size[1]):
    box = 0, y, im.size[0], y+1 # box bounding row y �趨�߽磬����ѡ��һ��
    row = im.crop(box) # ���߽������һ��
    bytes = row.tostring() # ����������ת��Ϊstring
    # Rotate 195 to the first column.
    i = bytes.index(magic) # ȷ����һ����ɫ��
    row = ImageChops.offset(row, -i) # ���ݵ�һ����ɫ���趨ƫ�ƣ���ɶ���
    im.paste(row, box)  # overwrite the original row ����ԭ������
im.save(r"mozartout.gif")  # or just "im.show()" ����Ϊ��һ���ļ�

