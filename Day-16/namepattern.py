''' ABCDEFGHIJKLMNOPQRSTUVWXYZ
(O)
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-------------------------------------------
(B)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-------------------------------
(E)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-------------------------------
(F)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j== 0 or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
--------------------------------
(C)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
---------------------------
(G)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
--------------------------------
(z)

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i == n-1 or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
--------------------------------------
(y)

n =  int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
------------------------------

(k)
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i==j and i>m) or (i+j == n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
----------------------------------------

(M)
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range (n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
--------------------------------------
(x)
n = int(input("Enter the size:  "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
-----------------------------------------
'''
