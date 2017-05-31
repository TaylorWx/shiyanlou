#coding=gbk
import calendar
def level_15():
        some=[]
        for i in range(10):
                for j in range(10):
                        some.append(int('1%d%d6'%(i,j))) # 所有的可能

        for i in some:
                if calendar.weekday(i,1,26)==0:
                        # 1月26日那天是周一,weekday工作日的第一天
                        # 判断是否是闰年
                        if ((i/4.0==i//4.0) and (i/100.0!=i//100.0)) or (i/400.0==i//400.0): 
                                # 能被4整除但不能被100整除，或者能被400整除
                                print (i) # 输出 1176 1356 1576 1756 1976
                                # 提示明天买花，说明1月27日是某人的诞辰or祭日？ google那天都有谁的诞辰
                                # http://zh.wikipedia.org/wiki/1%E6%9C%8827%E6%97%A5
                                # 所谓不是最年轻而是第二年轻大概是指不是1976而是1756
                                # 最接近的1756年1月27日 奥地利作曲家莫扎特诞辰（1791年逝世）。==> 
                                #http://www.pythonchallenge.com/pc/return/mozart.html

level_15()
