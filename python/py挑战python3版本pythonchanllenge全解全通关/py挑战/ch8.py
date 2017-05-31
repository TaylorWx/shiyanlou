from PIL import Image
import re

img = Image.open('oxygen.png')
map_string = ''.join(map(lambda p: chr(int(sum(img.getpixel((p, 43))[:3])/3)), range(4, 607, 7)))
print(map_string)
print('\nKey Words: ', end='')
for i in re.finditer(r'\d+', map_string):
    print(chr(int(i.group())), end='')
else:
    print()

