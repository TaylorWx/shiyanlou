#!/usr/bin/env python3

n=int(input("enter the number of students:"))
data={}
Subjects=('Physics','Maths','History')
for i in range(0, n):

    name=input('enter the name of the students {}:' .format(i + 1))

    marks=[]
    for x in Subjects:
        marks.append(int(input('enter marks of {}:' .format(x))))

    data[name]=marks

for x, y in data.items():

    total = sum(y)
    print("{}'s total marks {}" .format(x, total))

    if total < 120:
        print(x, "failed :(")

    else:
        print(x, "passed :)")
