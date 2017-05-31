#!/usr/bin/env python3

import sys
from collections import Counter
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grade(self):
        return
class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    def get_grade(self,scores):
    
        p=0
        f=0
        for i in list(scores):
            if (i == 'D'):
                f +=1
            else:
                p +=1
        print("Pass: %s, Fail: %s" %(p,f))

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))
    
    def get_grade(self,scores):
        score_list = Counter(list(scores)).most_common(4)
        print(", ".join('%s: %s'%(k,v) for (k,v) in score_list))


op=sys.argv[1]

scores=sys.argv[2]

if op == 'teacher':

    t=Teacher('n','p')
    t.get_grade(scores)

else:

    s=Student('1','b','c')
    s.get_grade(scores)
