#coding=gbk
from PIL import Image,ImageChops
im = Image.open(r"mozart.gif")
magic = bytes([195])#原来只需要将chr(195)-->bytes就好
for y in range(im.size[1]):
    box = 0, y, im.size[0], y+1 # box bounding row y 设定边界，就是选定一行
    row = im.crop(box) # 按边界剪切下一行
    bytes = row.tostring() # 将此行数据转换为string
    # Rotate 195 to the first column.
    i = bytes.index(magic) # 确定第一个粉色点
    row = ImageChops.offset(row, -i) # 根据第一个粉色点设定偏移，完成对齐
    im.paste(row, box)  # overwrite the original row 覆盖原来的行
im.save(r"mozartout.gif")  # or just "im.show()" 保存为另一个文件

