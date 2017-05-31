#coding=gbk
from PIL import Image,ImageDraw

im = Image.open("white.gif")
new = Image.new("RGB", (200, 200))
draw = ImageDraw.Draw(new)
cx, cy = 0, 100
for frame in range(133):
    im.seek(frame)
    left, upper, right, lower = im.getbbox()
    dx = (left - 100)//2
    dy = (upper - 100)//2
    if cx:
        draw.point([cx, cy])
    cx += dx
    cy += dy
    if dx == dy == 0:
        cx += 25
        cy = 100
new.save(r'23_2_white.png','png')
