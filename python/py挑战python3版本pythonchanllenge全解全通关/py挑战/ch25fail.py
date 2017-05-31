#coding=gbk
from PIL import PngImagePlugin,ImageDraw
import math,time
from binascii import unhexlify

# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# ��24��
# from top to bottom
# �ø��ӵ�һ��mazeͼѽ
# ��ʼ�����԰�ɫΪ��·�ǰ�ɫΪǽ�ڣ�����ǰд����A*�㷨��·�������û��·��
# ����ϸ�Ŵ�ͼƬ�鿴��Ե��ԭ�����ϽǺ����½Ǹ���һ����ɫ����
# ��ô˵���Ǿ����԰�ɫΪǽ�ڷǰ�ɫΪ��·�ˣ��ٴ���·���ҵ���
# ��û��ͷ���ˣ���ʼҲ��ͨ·�����ͼ���ַ������ɶҲ����������
# �ο����ԣ�ԭ�������ν�·�������ȡ���ڵ����ص�rֵ�������ļ��С�
# ��ɵ��ļ��Ǹ�zip���򿪣������������ļ�maze.jpg��mybroken.zip������maze.jpg
# ���Ǹ�ͼƬ��������lake���� ==> http://www.pythonchallenge.com/pc/hex/lake.html
# ��mybroken.zip�������и�mybroken.gif�������޷��򿪣��ƺ�û���á�
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
            """���(x,y)�Ƿ���closedlist��"""
            return (x << 16) ^ y in self.closedlist
        def inOpenList(self,x,y):
            """���(x,y)�Ƿ���openlist��"""
            for i,n in enumerate(self.openlist):
                if n.x==x and n.y==y:
                    return i
            return -1
        def showPath(self,l,showmark):
            """��ʾ·��"""
            tm=[] # �����������㵽�յ��·�������б�
            for i in l:
                tm.append((i.x,i.y))
            if showmark: # ����ͼ����ʾ��·����
                f=PngImagePlugin.PngImageFile(r'maze.png')
                my=f.copy()
                draw=ImageDraw.Draw(my)
                draw.point(tm,showmark)# (0,0,255,255))
                my.save(r'maze_showpath.png','png')

            # ��·�������ȡ���ص�rֵ���浽zip�ļ���
            f=PngImagePlugin.PngImageFile(r'maze.png')
            fo=open(r'maze_1.zip','wb')
            data=[]
            for i in tm[1::2]: # �ӵڶ������ؿ�ʼ�����ȡ
                r,dummy,dummy,dummy=f.getpixel(i)
                data.append(r)
            import array
            data = array.array("B", data).tostring()
            fo.write(data)
            fo.close()

        def SubNode(self,node,to_x,to_y):
            """ ���ؽڵ�node����Ч�ӽڵ�"""
            subList=[(node.x,node.y-1),\
                (node.x-1,node.y),\
                (node.x+1,node.y),\
                (node.x,node.y+1),]
            for x,y in subList:
                if self.map[y][x] !='#': # ����ֵ��Ч
                    if not self.inCloseList(x,y): # ����closedlist��
                        item= Node(node,x,y,math.sqrt((x-to_x)*(x-to_x)+(y-to_y)*(y-to_y))*1.2)
                        item.g=item.parent.g+1.0
                        yield item

        def getPath(self,from_x,from_y,to_x,to_y,show_mark=None):
            """��ȡ������·��
            from_coord ���
            to_coord �յ�
            show_mark ������ʾ·������ɫ
            """
            print ("(%d,%d)->(%d,%d)"%(from_x,from_y,to_x,to_y))

            self.openlist.append(Node(None,from_x,from_y,0))
            while self.openlist: 
                # �ظ����µĹ�����
                # a) Ѱ�ҿ����б���Fֵ��͵ĸ��ӡ����ǳ���Ϊ��ǰ��
                minf,minidx,curCoord=1000000,-1,None 
                # ���赱ǰ����fΪ1000000
                for i,n in enumerate(self.openlist):
                    if n.g+n.h<minf:
                        minf=n.g+n.h
                        curCoord=n
                        minidx=i
                # b) �����л����ر��б�
                del self.openlist[minidx]
                self.closedlist.add(curCoord)

                # c) �����ڵ�8���е�ÿһ��
                for item in self.SubNode(curCoord,to_x,to_y):
                    # ��������ڿ����б��У�������ӽ�ȥ���ѵ�ǰ����Ϊ��һ��ĸ��ڵ㡣
                    # ��¼��һ���F,G,��Hֵ��
                    i=self.inOpenList(item.x,item.y)
                    if i==-1:
                        self.openlist.append(item)
                        # ����·������Ŀ���ʼ������ÿһ��ĸ��ڵ��ƶ�ֱ���ص���ʼ����������·����
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

                    # ������Ѿ��ڿ����б��У���GֵΪ�ο�����µ�·���Ƿ���á����͵�Gֵ
                    # ��ζ�Ÿ��õ�·����������������Ͱ���һ��ĸ��ڵ�ĳɵ�ǰ�񣬲���
                    # ���¼�����һ���G��Fֵ������㱣����Ŀ����б�Fֵ���򣬸ı�֮��
                    # �������Ҫ���¶Կ����б�����
                    else:
                        if item.g<self.openlist[i].g:
                            self.openlist[i].parent=curCoord
                            self.openlist[i].g=item.g


            print ("no path found!")
            return False

    # ׼����ͼ����
    f=PngImagePlugin.PngImageFile(r'maze.png')
    # ��mazeתΪ������ʽ����m
    m,line=[],[]
    for y in range(f.size[1]):
        for x in range(f.size[0]):
            if f.getpixel((x,y))==(255,255,255,255):
                line.append('#') # ��ɫΪǽ��
            else:
                line.append('.') # ����Ϊͨ·
        m.append(''.join(line))
        del line[:]

    # ����A*�㷨��·
    t=AStarTest(len(m[0]),len(m),m)
    t.getPath(639,0,1,640,(0,0,255,255))

level_24()
