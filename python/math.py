#!/usr/bin/env python3
n=int(input("enter the value of n: "))

print("enter values for the matria A")

a=[]

for i in range(n):
    
    a.append([ int (x) for x in input().split()])
 
print("enter values for the Matri B")

b=[]

for i in range(n):
   
    b.append([int(x) for x in input().split()])

c=[]

for i in range(n):

   c.append(a[i][j] * b[i][j] for j in range(n))

print("after matrix multiplication")

print(" _"*7*n)

for x in c:
    for y in x:
        
        print(str(y).rjust(5), end=' ')
    print()

print("_" *7 *n)
