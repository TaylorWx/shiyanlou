#coding=gbk
import calendar
def level_15():
        some=[]
        for i in range(10):
                for j in range(10):
                        some.append(int('1%d%d6'%(i,j))) # ���еĿ���

        for i in some:
                if calendar.weekday(i,1,26)==0:
                        # 1��26����������һ,weekday�����յĵ�һ��
                        # �ж��Ƿ�������
                        if ((i/4.0==i//4.0) and (i/100.0!=i//100.0)) or (i/400.0==i//400.0): 
                                # �ܱ�4���������ܱ�100�����������ܱ�400����
                                print (i) # ��� 1176 1356 1576 1756 1976
                                # ��ʾ�����򻨣�˵��1��27����ĳ�˵ĵ���or���գ� google���춼��˭�ĵ���
                                # http://zh.wikipedia.org/wiki/1%E6%9C%8827%E6%97%A5
                                # ��ν������������ǵڶ���������ָ����1976����1756
                                # ��ӽ���1756��1��27�� �µ���������Ī���ص�����1791����������==> 
                                #http://www.pythonchallenge.com/pc/return/mozart.html

level_15()
