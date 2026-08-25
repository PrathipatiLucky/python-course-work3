'''
i = 1
while i<=10:
    print(i)
    i+=1
-----------------------------
    
i = 10
while i>0:
    print(i)
    i-=1
---------------------------
    
i = 5
while i<=50:
    print(i)
    i+=5
---------------------------
s = 'while loop'
i = 10
while i<len(s):
    print(s[i])
    i+=1
--------------------------

s = 'while loop'
i = 10
while i>len(s):
    print(s[i])
    i-=1
--------------------------

n = 98765423456
while n>0:
    print(n%10)
    n//10
------------------------
n = 98765423456
while n>0:
    print(n%10)
    n//=10
-----------------------

n = 98765423456
sumofdigits = 0
while n>0:
    sumofdigits += n%10
    n//=10

print("sum of digits:",sumofdigits)
----------------------------------------

n = 87654345
proofdigits = 1
while n>0:
    proofdigits *= n%10
    n//=10

print("sum of digits:",proofdigits)
------------------------------------------

n = 34567
res=0
while n> 0:
    rem = n%10
    res = res*10 + rem
    n//=10

print(res)
-------------------
n = 34567
res=0
while n> 0:
    rem = n%10
    if rem%2==0:
        res+=rem
    n//=10
--------------------------

l =[7,9,23,0,0,0,12,0,13,0,1,0,4,0,1,0,0,1]
while 0 in l:
    l.remove(0)
print(l)
----------------------

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i,j = 0,len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
---------------------
'''

