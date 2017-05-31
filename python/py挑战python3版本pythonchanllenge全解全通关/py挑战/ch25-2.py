#coding=gbk
class MazeBase(object):
    def __init__(self):
        self._reset()

    def _reset(self):
        # List of (point, list of successor choices) pairs.
        # This captures the current path from the starting point;
        # the successor lists are used during backtracking.
        self.path = []

        # A point is on the current `path` iff it's in this set.
        self.onpath = set()

    # Subclass must override.  Return true iff `point` is a part of
    # the maze we can traverse (in bounds, and not part of "a wall").
    # It will never be called with a point already on the current
    # path.
    def is_feasible(self, point):
        raise NotImplementedError

# Return list of `point`'s traversable neighbors.  This
# implementation assumes all _possible_ neighbors are
# the four (x+/-1, y) and (x, y+/-1).  A subclass should
# override if the maze geometry doesn't work that way.
#invalid syntax?why?#here have to 替换(x,y)-->point,then,=
    def neighbors(self,point):
        x,y=point
        return [p for p in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]\
                if p not in self.onpath and self.is_feasible(p)]

    def add_to_path(self, point):
        assert point not in self.onpath
        self.onpath.add(point)
        self.path.append((point, self.neighbors(point)))

    # Generate all paths starting at point `start`.  The same
    # list object is yielded each time, so the caller should
    # copy what it wants if it lets the generator resume.
    def gen_paths(self, start):
        self._reset()
        assert self.is_feasible(start)
        self.add_to_path(start)
        path, onpath = self.path, self.onpath
        yield path
        while path:
            point, choices = path[-1]
            if choices:
                self.add_to_path(choices.pop())
                yield path
            else:   
                #估计就是走迷宫没有路了
                # out of choices here -- backtrack
                del path[-1]
                onpath.remove(point)

from PIL import Image
im = Image.open("maze.png")

black = 0, 0, 0, 255
white = 255, 255, 255, 255
blue = 0, 0, 255, 255


class Level24(MazeBase):
    def __init__(self, image):
        super(Level24, self).__init__()
        self.im = image
        self.xn, self.yn = image.size

    def is_feasible(self, point):
        return (0 <= point[0] < self.xn and
                0 <= point[1] < self.yn and
                self.im.getpixel(point) != white)

    def solve(self):
        self.solution = None # nothing yet
        # "from top to bottom" suggests we need to start in
        # row 0 and end in row yn-1.
        last_row = self.yn - 1
        for x in range(self.xn):
            if self.im.getpixel((x, 0)) == black:
                for path in self.gen_paths((x, 0)):
                    if path[-1][0][1] != last_row:
                        continue
                    if self.solution is not None:
                        # It would be an ambiguous puzzle if
                        # more than one such is found.
                        raise ValueError("multiple solutions")
                    self.solution = [p[0] for p in path]
                    # If you want to assume the solution is
                    # unique, put a `return` here, and it will
                    # run about twice as fast.

m = Level24(im)
m.solve()

from PIL import ImageDraw
im2 = im.copy()
ImageDraw.Draw(im2).point(m.solution, blue)
im2.save("twisty.png")

im2.paste(white)
ImageDraw.Draw(im2).point(m.solution, blue)
im2.save("justblue.png")

data = []
for p in m.solution:
    r, g, b, a = im.getpixel(p)
    assert g == b == 0 and a == 255
    data.append(r)
import array
data = array.array("B", data).tostring()
# That's the same as data = "".join(map(chr, data)), but faster for
# "large" len(data).

d1 = data[0::2]
assert d1 == b"\x00" * len(d1)

d2 = data[1::2]
f = open("hidden.zip", "wb")
f.write(d2)
f.close()
#There's still something peculiar here: while many programs can open that zip file, Python's zipfile module cannot:

#import zipfile
#z = zipfile.ZipFile("hidden.zip", "r")
