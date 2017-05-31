#coding=gbk

    # ���ϲ���һ�£����ָ����������������Ϣ��ԭ����ͼ����Ϸ�и�ר�ŵ����ƽ�Nonogram
    # �� http://zh.wikipedia.org/zh-cn/Nonogram
    # ��ɳ���Ĺ��̱Ƚ����ۣ�
    # 1��һ��ʼ������9*9��Сͼ����ֱ����0-512ö������ÿ��ÿ�еĿ��ܣ�
    # Ȼ������ٵķ�ʽͨ������ƥ����ԣ��õ��˻����ϼ�ͷ��ͼ ==> http://www.pythonchallenge.com/pc/rock/up.html
    # ��ʱ�õ�����Ҫ��ԭ��ͼ�� 32*32 �Ĵ�ͼ��ԭ��������ÿ��ÿ�п������еķ�����Ч��̫�ͣ�û�����ˣ�
    # 2��Ȼ���÷ǵݹ鷽ʽд������ÿ��ÿ�п������е��·�����genlist()���������ڽ������ʱ������
    # ��Ҫ��ٵĴ����Ǹ����������ˣ����������ܶ�ʱ������������
    # 3��������ϸ�о�����ʼ�����ȴ����еĿ��������еõ���ȷ�������ջ������ĵ㣬�ٸ�����Щ�㷴�����ٴι�������
    # ������ȥ�������ϵ����У�Ȼ���ٸ��ݱ����µĿ��������ٴεõ���ȷ�����µ�����/���ĵ㣬������Щ�㷴����
    # ���˵������ϵ����У���˷������� ȷ������/����->���˲���������->ȷ���µ�����/���㣬����26�κ�
    # ���ڽ�32*32���㶼ȷ�������յõ��������ߵ�ͼ��
    # 4������ĳ�����Ҫִ�н�22�룬�����Ż��󣬵���ִ�д����Ҫ��2�룬�������⡣�����ӹ����п�����
    # ͨ���ݹ�����ÿ��ÿ�п������еĺ�����genv()������΢�޸ľ��������ˣ���genlist()Ҫ��0.5�롣
    # ���ڵĳ��������32*32������ͼ��ҪԼ1.5��(test3())��
    # 5�����ǵ�Ӧ�þ��������/����ȷ���ĵ�Ϊ�����������ٶ�Ӧ��/�еĿ������У��������Լ��ٵ������������Ҽ��ٺ�������
    # ����Ҫ�߼�����һ�𣬾�����32*32��ҪԼ1.3��(test4())
    # ��������ͼ ==> http://www.pythonchallenge.com/pc/rock/python.html
    # ps: ֵ��ע������ҳҲ�����˽��������ͼjs���루http://www.pythonchallenge.com/pc/rock/python.js��
    # ��ҳ��ʾ��
    # Congrats! You made it through to the smiling python.
    # "Free" as in "Free speech", not as in "free...
    #
    # ����ÿ�����ʶ���ʶ���������ɶ��˼��֪��:(��google֮
    # �� ��Free as in Free speech, not as in free���ѵ���һ����
    # http://www.gnu.org/philosophy/free-sw.html �е�
    # "Free software" is a matter of liberty, not price. To understand the concept, you should think of "free" as in "free speech," not as in "free beer."
    # ������˼��˵�������ָȨ���ϵ����ɶ�����ָ��ѡ�Ҫ�����һ�㣬����ԱȽϡ������ݽ����͡����ơ�ơ��е�free������
    # ������ʾ��"free..."�е�"..."ָ���� beer ==> http://www.pythonchallenge.com/pc/rock/beer.html
def level_32():
    def test3(width,height):
        UNKNOWN,FILL,EMPTY='?','1',' '
        resovled=[[UNKNOWN for _ in range(width)] for _ in range(height)]
        totalnumber=width*height
        print (totalnumber)
        def genv(v,l,marks):
            '''�ݹ鷽ʽ��ȡ���ܵ�����
            v=������(tuple�б�) l=��/�г��� marks=(����,����)
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
    # �ǵݹ鷽ʽ��ȡ���ܵ����У�������ݹ鷽ʽ��genvҪ��һ��
        def genlist(dim,blocklist,marks=('1','0')):
            '''�ǵݹ鷽ʽ��ȡ���ܵ�����
            dim=��/�г��� blocklist=������(tuple�б�) marks=(����,����)
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
    # ��Ҫ��λ
                    tmp=cur-1 
    # ��һλ
                    while tmp!=-1: 
    # tmp=-1 ��λ�ɽ���˵���о���ϣ��˳�
                        if idxl[tmp]<blankcnt-(blockcnt-tmp-1)-sum(idxl[:tmp]): 
    # ��λ����������1
                            idxl[tmp]+=1
                            for i in range(tmp+1,blockcnt):
                                idxl[i]=1
                            idxl[-1]=blankcnt-sum(idxl[:-1])
                            break
                        else: 
    # ��λ���������ӣ���Ҫ�鿴��ǰ��һλ
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
            '''���l������item�ĵ�idx���Ƿ�һ�£���һ���򷵻�None�����򷵻������ֵ'''
            for item in l:
                if item[idx]!=l[0][idx]:
                    return None
            return l[0][idx]
        def confirmed():
            '''�������е�Hlist Vlist������ȷ���Ŀ飬��resovled�б���������ذ�����Щ��ȷ���Ŀ���б�'''
            ret=[]
    # ����������ȷ����
            for i,rows in enumerate(Hlist):
                for j in range(width):
                    if resovled[i][j]==UNKNOWN:
                        t= checksingle(j,rows)
                        if t:
                            resovled[i][j]=t
                            ret.append((i,j))
    # ����������ȷ����
            for i,cols in enumerate(Vlist):
                for j in range(height):
                    if resovled[j][i]==UNKNOWN:
                        t= checksingle(j,cols)
                        if t:
                            resovled[j][i]=t
                            ret.append((j,i))
            return ret
        def reducePossible(obj2check):
            '''����obj2check���˲����������Ŀ�������'''
            for i,j in obj2check:
    # �й���
                c=resovled[i][j] 
    # �д��м������ʹ�����0.05s
                Hlist[i]=[item for item in Hlist[i] if item[j]==c]
    # �й���
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
            '''���l������item�ĵ�idx���Ƿ�һ�£���һ���򷵻�None�����򷵻������ֵ'''
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
    # ������ȷ���ĵ�������Vlist��Ӧ�еĿ�������
                            resovlednumber+=1
            for i,cols in enumerate(Vlist):
                for j in range(height):
                    if resovled[j][i]==UNKNOWN:
                        t= checksingle(j,cols)
                        if t:
                            resovled[j][i]=t
                            Hlist[j]=[item for item in Hlist[j] if item[i]==t] 
    # ������ȷ���ĵ�������Hlist��Ӧ�еĿ�������
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
