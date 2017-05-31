#coding=gbk
import dijkstra,pickle
from PIL import Image

"""dijkstra.py requires a dictionary-like object for access to vertices and edges"""
class G:
    def __init__(self, imgdata, imgsize):
        self.imgdata = imgdata
        self.width, self.height = imgsize
    def __getitem__(self, vertex):
        """return dict containing edges and corresponding weights"""
        x, y = vertex
        # All neighbours
        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        # Filter out pixels outside of image
        neighbours = [(nx, ny) for (nx, ny) in neighbours
                      if 0 <= nx < self.width and 0 <= ny < self.height]
        # Keep only non-white pixels
        neighbours = [(nx, ny) for (nx, ny) in neighbours
                      if self.imgdata[nx + ny*self.width][1] == 0]
        return dict([(n, 1) for n in neighbours])  # Attach arbitrary weight to the edges

"""Phase 1: extract path from image"""
def phase1():                    
    img = Image.open('maze.png')
    data = list(img.getdata())
    start = 639, 0
    end = 1, 640
    g = G(data, img.size)
    print ('Dijkstra...')
    D, P = dijkstra.Dijkstra(g, start, end)
    # Construct path from P; add color values in the same pass
    print ('Constructing path...')
    path = []
    pos = end
    while True:
        x, y = pos
        path.append((pos, data[x+img.size[0]*y][0]))
        if pos == start:
            break
        pos = P[pos]
    path.reverse()
    # Save the sequence to file, so we can study it without having to
    # recalculate it again and again
    pickle.dump(path, open('maze.sequence', 'wb'))
    print ('path pickled as maze.sequence')

"""Phase 2: generate zipfile from data"""
def phase2():
    path = pickle.load(open('maze.sequence', 'rb'))
    # Some investigation suggests that only the red values are relevant
    reds = [r for (pos, r) in path]
    # First I tried using all the red pixels and not the black (i.e. only the
    # pixels with non-zero values), but that resulted in a corrupt file. The
    # correct way is simply to take every second value, starting from the second
    # one.
    data = reds[1::2]
    import array
    data = array.array("B", data).tostring()
    open('maze.zip', 'wb').write(data)

# Execute
phase1()
phase2()
