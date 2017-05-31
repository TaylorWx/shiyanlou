#coding=gbk

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
    #   assert sum(sum(x) for x in Horizontal)==sum(sum(x) for x in Vertical)
    #
    #   Hlist=[genlist(width,item,(FILL,EMPTY)) for item in Horizontal]
    #
    #   Vlist=[genlist(height,item,(FILL,EMPTY)) for item in Vertical]
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
    #       print (out)
            itercnt+=1
        print ( '\n'.join([''.join(j) for j in resovled]))
        print ('%s done! %s'%('='*30,'='*30))
    Horizontal=((2,1,2),(1,3,1),(5,),(7,),(9,),(3,),(2,3,2),(2,3,2),(2,3,2))
    Vertical=((2,1,3),(1,2,3),(3,),(8,),(9,),(8,),(3,),(1,2,3),(2,1,3))
    test3(9,9)
    Horizontal=((3,2),(8,),(10,),(3,1,1),(5,2,1),(5,2,1),(4,1,1),(15,),(19,),(6,14),(6,1,12),(6,1,10),(7,2,1,8),(6,1,1,2,1,1,1,1),(5,1,4,1),(5,4,1,4,1,1,1),(5,1,1,8),(5,2,1,8),(6,1,2,1,3),(6,3,2,1),(6,1,5),(1,6,3),(2,7,2),(3,3,10,4),(9,12,1),(22,1),(21,4),(1,17,1),(2,8,5,1),(2,2,4),(5,2,1,1),(5,))
    Vertical=((5,),(5,),(5,),(3,1),(3,1),(5,),(5,),(6,),(5,6),(9,5),(11,5,1),(13,6,1),(14,6,1),(7,12,1),(6,1,11,1),(3,1,1,1,9,1),(3,4,10),(8,1,1,2,8,1),(10,1,1,1,7,1),(10,4,1,1,7,1),(3,2,5,2,1,2,6,2),(3,2,4,2,1,1,4,1),(2,6,3,1,1,1,1,1),(12,3,1,2,1,1,1),(3,2,7,3,1,2,1,2),(2,6,3,1,1,1,1),(12,3,1,5),(6,3,1),(6,4,1),(5,4),(4,1,1),(5,))
    test3(32,32)
level_32()
