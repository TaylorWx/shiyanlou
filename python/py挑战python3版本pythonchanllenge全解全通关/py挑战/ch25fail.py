#coding=gbk
from PIL import PngImagePlugin,ImageDraw
import math,time
from binascii import unhexlify

# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# 第24关
# from top to bottom
# 好复杂的一张maze图呀
# 开始试着以白色为道路非白色为墙壁，用以前写过的A*算法找路径，结果没有路。
# 又仔细放大图片查看边缘，原来右上角和左下角各有一个黑色像素
# 这么说就是就是以白色为墙壁非白色为道路了，再次找路，找到。
# 又没有头绪了，开始也许通路能组成图形字符，结果啥也看不出来。
# 参考攻略，原来是依次将路径间隔着取所在的像素的r值，存入文件中。
# 存成的文件是个zip，打开，里面有两个文件maze.jpg和mybroken.zip，其中maze.jpg
# 打开是个图片，上面有lake字样 ==> http://www.pythonchallenge.com/pc/hex/lake.html
# 而mybroken.zip打开里面有个mybroken.gif，不过无法打开，似乎没有用。
def level_24():
    class Node:
        def __init__(self,parent,x,y,h):
            self.parent=parent
            self.x,self.y=x,y
            self.hv = (x << 16) ^ y
            self.g,self.h=0,h
        def __repr__(self):
            return '(%d,%d)'%(self.x,self.y)
        def __eq__(self,other):
            return self.hv == other
        def __hash__(self):
            return self.hv

    class AStarTest:
        def __init__(self,map_max_x,map_max_y,map):
            self.openlist,self.closedlist=[],set()
            self.mapMaxX,self.mapMaxY=map_max_x,map_max_y
            print ('%d %d'%(self.mapMaxX,self.mapMaxY))
            self.map=map
        def inCloseList(self,x,y):
            """检查(x,y)是否在closedlist中"""
            return (x << 16) ^ y in self.closedlist
        def inOpenList(self,x,y):
            """检查(x,y)是否在openlist中"""
            for i,n in enumerate(self.openlist):
                if n.x==x and n.y==y:
                    return i
            return -1
        def showPath(self,l,showmark):
            """显示路径"""
            tm=[] # 用来保存从起点到终点的路径坐标列表
            for i in l:
                tm.append((i.x,i.y))
            if showmark: # 在新图中显示出路径来
                f=PngImagePlugin.PngImageFile(r'maze.png')
                my=f.copy()
                draw=ImageDraw.Draw(my)
                draw.point(tm,showmark)# (0,0,255,255))
                my.save(r'maze_showpath.png','png')

            # 将路径间隔着取像素的r值保存到zip文件中
            f=PngImagePlugin.PngImageFile(r'maze.png')
            fo=open(r'maze_1.zip','wb')
            data=[]
            for i in tm[1::2]: # 从第二个像素开始间隔着取
                r,dummy,dummy,dummy=f.getpixel(i)
                data.append(r)
            import array
            data = array.array("B", data).tostring()
            fo.write(data)
            fo.close()

        def SubNode(self,node,to_x,to_y):
            """ 返回节点node的有效子节点"""
            subList=[(node.x,node.y-1),\
                (node.x-1,node.y),\
                (node.x+1,node.y),\
                (node.x,node.y+1),]
            for x,y in subList:
                if self.map[y][x] !='#': # 坐标值有效
                    if not self.inCloseList(x,y): # 不在closedlist中
                        item= Node(node,x,y,math.sqrt((x-to_x)*(x-to_x)+(y-to_y)*(y-to_y))*1.2)
                        item.g=item.parent.g+1.0
                        yield item

        def getPath(self,from_x,from_y,to_x,to_y,show_mark=None):
            """获取两点间的路径
            from_coord 起点
            to_coord 终点
            show_mark 用来显示路径的颜色
            """
            print ("(%d,%d)->(%d,%d)"%(from_x,from_y,to_x,to_y))

            self.openlist.append(Node(None,from_x,from_y,0))
            while self.openlist: 
                # 重复如下的工作：
                # a) 寻找开启列表中F值最低的格子。我们称它为当前格。
                minf,minidx,curCoord=1000000,-1,None 
                # 假设当前最新f为1000000
                for i,n in enumerate(self.openlist):
                    if n.g+n.h<minf:
                        minf=n.g+n.h
                        curCoord=n
                        minidx=i
                # b) 把它切换到关闭列表。
                del self.openlist[minidx]
                self.closedlist.add(curCoord)

                # c) 对相邻的8格中的每一个
                for item in self.SubNode(curCoord,to_x,to_y):
                    # 如果它不在开启列表中，把它添加进去。把当前格作为这一格的父节点。
                    # 记录这一格的F,G,和H值。
                    i=self.inOpenList(item.x,item.y)
                    if i==-1:
                        self.openlist.append(item)
                        # 保存路径。从目标格开始，沿着每一格的父节点移动直到回到起始格。这就是你的路径。
                        if item.x==to_x and item.y==to_y:
                            print ("found %d,len(closedlist)=%d"%(item.g,len(self.closedlist)))
                            l=[item]
                            p=item.parent
                            while p:
                                l.append(p)
                                p=p.parent
                            l.reverse()
                            self.showPath(l,show_mark)
                            return True

                    # 如果它已经在开启列表中，用G值为参考检查新的路径是否更好。更低的G值
                    # 意味着更好的路径。如果是这样，就把这一格的父节点改成当前格，并且
                    # 重新计算这一格的G和F值。如果你保持你的开启列表按F值排序，改变之后
                    # 你可能需要重新对开启列表排序。
                    else:
                        if item.g<self.openlist[i].g:
                            self.openlist[i].parent=curCoord
                            self.openlist[i].g=item.g


            print ("no path found!")
            return False

    # 准备地图数据
    f=PngImagePlugin.PngImageFile(r'maze.png')
    # 将maze转为数组形式存入m
    m,line=[],[]
    for y in range(f.size[1]):
        for x in range(f.size[0]):
            if f.getpixel((x,y))==(255,255,255,255):
                line.append('#') # 白色为墙壁
            else:
                line.append('.') # 其他为通路
        m.append(''.join(line))
        del line[:]

    # 调用A*算法找路
    t=AStarTest(len(m[0]),len(m),m)
    t.getPath(639,0,1,640,(0,0,255,255))

level_24()
