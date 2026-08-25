'''
for i in range(5):
    for j in range(5):
        print('*',end ='')
    print()
-----------------------------
    
for i in range(5):
    for j in range(5):
        print(j%2,end ='')
    print()
------------------------

for i in range(5):
    for j in range(5):
        print(i%2,end ='')
    print()
-----------------------------

for i in range(5):
    for j in range(5):
        print((i+j)%2,end ='')
    print()


for i in range(5):
    for j in range(5):
        print(i+j,end='')
    print()
--------------------------

c=1
for i in range(5):
    for j in range(5):
        print(c, end='')
        c+=1
    print()
------------------------

for i in range(5):
    for j in range(i+1):
        print('7',end='')
    print()
-------------------------------

for i in range (5):
    for j in range(5-i):
        print('*',end='')
    print()
------------------------------

for i in range (5):
    for sp in range(5-i-1):
        print('',end='')
    for j in range(i+1):
        print("*",end='')
    print()

n = int(input("Enter the size: "))
for i in range(n):
    for sp in range (i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()
-------------------------------

n =int(input("Enter the Size: "))
m = n//2
for i in range(n):
    if i <=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for k in range(n-i):
            print('*',end=' ')
    print()
--------------------------------------

n =int(input("Enter the Size: "))
m = n//2
for i in range(n):
    if i <=m:
        print('* '*(i+1),end=' ')
    else:
        print('* '*(n-i),end=' ')
    print()
--------------------------------------

m = int(input("Enter the size: "))
n = n//2
for i in range(n):
    if i <=m:
        print(' '*(m-i),'* '*(i+1),end=' ',sep='')
    else:
        print(' '*(i-m),'* '*(n-i),end=' ',sep='')
    print()
----------------------------------------------------

num = 1

for i in range(5):
    row = []

    for j in range(5):
        row.append(num)
        num += 1

    if i % 2 == 1:
        row.reverse()

    for value in row:
        print(value, end="\t")

    print()

---------------------------------------
'''
