#coding=gbk
from PIL import Image
import time
im = Image.open('maze.png')
X, Y = im.size

MARK = 255
MARKER = MARK, MARK, MARK, 255

def is_wall(x, y):
    # Border.
    if x < 0 or x >= X or y < 0 or y >= Y:
        return True
    p1, p2, p3, p4 = im.getpixel((x, y))
    # White or marked is a wall.
    return p1 == p2 and p1 in (127, 255)

# If 'dead end' return the only possible direction, else None.
# Start flag to ignore start and end point (these are also 'dead ends').
def is_dead_end(x, y, start=True):
    # Possible start or finish (top/bottom).
    if start and (y == Y - 1 or y == 0):
        return None
    if is_wall(x, y):
        return None
    direction = None
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not is_wall(x + dx, y + dy):
            if direction:
                # More than one way out:  not a dead end.
                return None
            direction = dx, dy
    return direction

def dead_end_filler(x, y, start=True):
    out = []
    direction = is_dead_end(x, y, start)
    import array
    while direction:
        out1= bytes(im.getpixel((x, y)))[0]#chr
        out.append(out1)
        im.putpixel((x, y), MARKER)
        dx, dy = direction
        x, y = x + dx, y + dy
        direction = is_dead_end(x, y, start)
    return out

def scan(x, y):	
    for j in range(y):
        for i in range(x):
            if not is_wall(i, j):
                dead_end_filler(i, j)

scan(X, Y)
im.save('maze.solved.png')

out = dead_end_filler(639, 0, False)

f = open('maze24.zip', 'wb')
data=out[1::2]
import array
data = array.array("B", data).tostring()
#for item in out:
#    print(item)
#import array
#out=array.frombytes(out)

f.write(data)
f.close()
