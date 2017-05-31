#coding=gbk

    # 网上查了一下，这种根据行列连续块的信息还原点阵图的游戏有个专门的名称叫Nonogram
    # 见 http://zh.wikipedia.org/zh-cn/Nonogram
    # 完成程序的过程比较曲折：
    # 1）一开始看到是9*9的小图，就直接用0-512枚举生成每行每列的可能，
    # 然后用穷举的方式通过正则匹配测试，得到了画着上箭头的图 ==> http://www.pythonchallenge.com/pc/rock/up.html
    # 此时得到的需要还原的图是 32*32 的大图，原来的生成每行每列可能排列的方法的效率太低，没法用了；
    # 2）然后用非递归方式写出生成每行每列可能排列的新方法（genlist()），但是在进行穷举时，发现
    # 需要穷举的次数是个天文数字了，根本不可能短时间内算出结果；
    # 3）经过仔细研究，开始尝试先从现有的可能排列中得到能确定是留空还是填充的点，再根据这些点反过来再次过滤所有
    # 可能以去掉不符合的排列，然后再根据保留下的可能排列再次得到能确定的新的留空/填充的点，再用这些点反过来
    # 过滤掉不符合的排列，如此反复进行 确定留空/填充点->过滤不符合排列->确定新的留空/填充点，经过26次后
    # 终于将32*32个点都确定，最终得到画着蟒蛇的图；
    # 4）最初的程序需要执行近22秒，经过优化后，单独执行大概需要近2秒，基本满意。后来从攻略中看到了
    # 通过递归生成每行每列可能排列的函数（genv()），稍微修改就拿来用了，比genlist()要快0.5秒。
    # 现在的程序算这个32*32的蟒蛇图需要约1.5秒(test3())。
    # 5）考虑到应该尽早的以行/列新确定的点为过滤条件减少对应列/行的可能排列，这样可以减少迭代次数，并且减少函数调用
    # 将主要逻辑放在一起，经测试32*32需要约1.3秒(test4())
    # 根据蟒蛇图 ==> http://www.pythonchallenge.com/pc/rock/python.html
    # ps: 值得注意是网页也给出了解出的蟒蛇图js代码（http://www.pythonchallenge.com/pc/rock/python.js）
    # 网页提示：
    # Congrats! You made it through to the smiling python.
    # "Free" as in "Free speech", not as in "free...
    #
    # 上面每个单词都认识，组合起来啥意思不知道:(，google之
    # 搜 “Free as in Free speech, not as in free”搜到第一条是
    # http://www.gnu.org/philosophy/free-sw.html 中的
    # "Free software" is a matter of liberty, not price. To understand the concept, you should think of "free" as in "free speech," not as in "free beer."
    # 好像意思是说自由软件指权利上的自由而不是指免费。要理解这一点，你可以比较“自由演讲”和“免费啤酒”中的free的区别。
    # 所以提示中"free..."中的"..."指的是 beer ==> http://www.pythonchallenge.com/pc/rock/beer.html
def level_32():
    def test3(width,height):
        UNKNOWN,FILL,EMPTY='?','1',' '
        resovled=[[UNKNOWN for _ in range(width)] for _ in range(height)]
        totalnumber=width*height
        print (totalnumber)
        def genv(v,l,marks):
            '''递归方式获取可能的排列
            v=描述串(tuple列表) l=行/列长度 marks=(填满,留空)
            '''
            r=[]
            j=0
            if v:
                if len(v)==1:
                    j=1
                for i in range(l+2-len(v)-sum(v)):
                    ri=marks[1]*i+marks[0]*v[0]+marks[1]*(1-j)
                    if j:
                        rr=[marks[1]*(l-len(ri))]
                    else:
                        rr=genv(v[1:],l-len(ri),marks)
                    r+=[ri+vv for vv in rr]
                return r
            else:
                return [marks[1]*l]
    # 非递归方式获取可能的排列，比上面递归方式的genv要慢一点
        def genlist(dim,blocklist,marks=('1','0')):
            '''非递归方式获取可能的排列
            dim=行/列长度 blocklist=描述串(tuple列表) marks=(填满,留空)
            '''
            ret=[]
            blankcnt=dim-sum(blocklist)
            blockcnt=len(blocklist)
            idxl=[1 for i in range(blockcnt+1)]
            idxl[0]=0
            idxl[-1]=blankcnt-(blockcnt-1)
            cur=len(idxl)-2
            tmp=cur
            while tmp!=-1:
                tmpstr=''.join([ marks[1]*idxl[x]+marks[0]*blocklist[x] for x in range(blockcnt)]+[marks[1]*idxl[-1],])
                ret.append(tmpstr)
                if idxl[-1]==0: 
    # 需要进位
                    tmp=cur-1 
    # 上一位
                    while tmp!=-1: 
    # tmp=-1 无位可进，说明列举完毕，退出
                        if idxl[tmp]<blankcnt-(blockcnt-tmp-1)-sum(idxl[:tmp]): 
    # 此位可以再增加1
                            idxl[tmp]+=1
                            for i in range(tmp+1,blockcnt):
                                idxl[i]=1
                            idxl[-1]=blankcnt-sum(idxl[:-1])
                            break
                        else: 
    # 此位不能再增加，需要查看更前的一位
                            tmp-=1
                else:
                    idxl[cur]+=1
                    for i in range(cur+1,blockcnt):
                        idxl[i]=1
                    idxl[-1]=blankcnt-sum(idxl[:-1])
            return ret
    #
    #    assert sum(sum(x) for x in Horizontal)==sum(sum(x) for x in Vertical)
    #
    #    Hlist=[genlist(width,item,(FILL,EMPTY)) for item in Horizontal]
    #
    #    Vlist=[genlist(height,item,(FILL,EMPTY)) for item in Vertical]
        Hlist=[genv(a,width,(FILL,EMPTY)) for a in Horizontal]
        Vlist=[genv(a,height,(FILL,EMPTY)) for a in Vertical]
        print ('all possible row/col generated.')
        def checksingle(idx,l):
            '''检查l中所有item的第idx项是否一致，不一致则返回None，否则返回这项的值'''
            for item in l:
                if item[idx]!=l[0][idx]:
                    return None
            return l[0][idx]
        def confirmed():
            '''根据现有的Hlist Vlist搜索可确定的块，在resovled中标出，并返回包含这些新确定的块的列表'''
            ret=[]
    # 按行搜索可确定块
            for i,rows in enumerate(Hlist):
                for j in range(width):
                    if resovled[i][j]==UNKNOWN:
                        t= checksingle(j,rows)
                        if t:
                            resovled[i][j]=t
                            ret.append((i,j))
    # 按列搜索可确定块
            for i,cols in enumerate(Vlist):
                for j in range(height):
                    if resovled[j][i]==UNKNOWN:
                        t= checksingle(j,cols)
                        if t:
                            resovled[j][i]=t
                            ret.append((j,i))
            return ret
        def reducePossible(obj2check):
            '''根据obj2check过滤不符合条件的可能排列'''
            for i,j in obj2check:
    # 行过滤
                c=resovled[i][j] 
    # 有此中间变量可使程序快0.05s
                Hlist[i]=[item for item in Hlist[i] if item[j]==c]
    # 列过滤
                Vlist[j]=[item for item in Vlist[j] if item[i]==c]
            print ('H after: ',)
            print (','.join([str(len(x)) for x in Hlist]))
            print ('V after: ',)
            print (','.join([str(len(x)) for x in Vlist]))
        resovlednumber=0
        itercnt=1
        while resovlednumber!=totalnumber:
            print ('itercnt=%d'%(itercnt,))
            tocheck=confirmed()
            if len(tocheck)==0:
                print ('no more number can confirm! %d'%(resovlednumber,))
                break
            resovlednumber+=len(tocheck)
            reducePossible(tocheck)
            print ('resolved number: %d'%(resovlednumber,))
    #
    #        print (out)
            itercnt+=1
        print (   '\n'.join([''.join(j) for j in resovled]))
        print ('%s done! %s'%('='*30,'='*30))
    def test4(width,height):
        UNKNOWN,FILL,EMPTY='?','1',' '
        resovled=[[UNKNOWN for _ in range(width)] for _ in range(height)]
        totalnumber=width*height
        print (totalnumber)
        def genv(v,l,marks):
            r=[]
            j=0
            if v:
                if len(v)==1:
                    j=1
                for i in range(l+2-len(v)-sum(v)):
                    ri=marks[1]*i+marks[0]*v[0]+marks[1]*(1-j)
                    if j:
                        rr=[marks[1]*(l-len(ri))]
                    else:
                        rr=genv(v[1:],l-len(ri),marks)
                    r+=[ri+vv for vv in rr]
                return r
            else:
                return [marks[1]*l]
        def checksingle(idx,l):
            '''检查l中所有item的第idx项是否一致，不一致则返回None，否则返回这项的值'''
            for item in l:
                if item[idx]!=l[0][idx]:
                    return None
            return l[0][idx]
        Hlist=[genv(a,width,(FILL,EMPTY)) for a in Horizontal]
        Vlist=[genv(a,height,(FILL,EMPTY)) for a in Vertical]
        print ('all possible row/col generated.')
        resovlednumber=0
        itercnt=1
        while resovlednumber!=totalnumber:
            print ('\nitercnt=%d'%(itercnt,))
            for i,rows in enumerate(Hlist):
                for j in range(width):
                    if resovled[i][j]==UNKNOWN:
                        t=checksingle(j,rows)
                        if t:
                            resovled[i][j]=t
                            Vlist[j]=[item for item in Vlist[j] if item[i]==t] 
    # 马上用确定的点来减少Vlist对应列的可能数量
                            resovlednumber+=1
            for i,cols in enumerate(Vlist):
                for j in range(height):
                    if resovled[j][i]==UNKNOWN:
                        t= checksingle(j,cols)
                        if t:
                            resovled[j][i]=t
                            Hlist[j]=[item for item in Hlist[j] if item[i]==t] 
    # 马上用确定的点来减少Hlist对应行的可能数量
                            resovlednumber+=1
            print ('H after: ',)
            print (','.join([str(len(x)) for x in Hlist]))
            print ('V after: ',)
            print (','.join([str(len(x)) for x in Vlist]))
            itercnt+=1
        print (   '\n'.join([''.join(j) for j in resovled]))
        print ('%s done! %s'%('='*30,'='*30))
    Horizontal=((2,1,2),(1,3,1),(5,),(7,),(9,),(3,),(2,3,2),(2,3,2),(2,3,2))
    Vertical=((2,1,3),(1,2,3),(3,),(8,),(9,),(8,),(3,),(1,2,3),(2,1,3))
    test4(9,9)
    Horizontal=((3,2),(8,),(10,),(3,1,1),(5,2,1),(5,2,1),(4,1,1),(15,),(19,),(6,14),(6,1,12),(6,1,10),(7,2,1,8),(6,1,1,2,1,1,1,1),(5,1,4,1),(5,4,1,4,1,1,1),(5,1,1,8),(5,2,1,8),(6,1,2,1,3),(6,3,2,1),(6,1,5),(1,6,3),(2,7,2),(3,3,10,4),(9,12,1),(22,1),(21,4),(1,17,1),(2,8,5,1),(2,2,4),(5,2,1,1),(5,))
    Vertical=((5,),(5,),(5,),(3,1),(3,1),(5,),(5,),(6,),(5,6),(9,5),(11,5,1),(13,6,1),(14,6,1),(7,12,1),(6,1,11,1),(3,1,1,1,9,1),(3,4,10),(8,1,1,2,8,1),(10,1,1,1,7,1),(10,4,1,1,7,1),(3,2,5,2,1,2,6,2),(3,2,4,2,1,1,4,1),(2,6,3,1,1,1,1,1),(12,3,1,2,1,1,1),(3,2,7,3,1,2,1,2),(2,6,3,1,1,1,1),(12,3,1,5),(6,3,1),(6,4,1),(5,4),(4,1,1),(5,))
    test4(32,32)

level_32()
