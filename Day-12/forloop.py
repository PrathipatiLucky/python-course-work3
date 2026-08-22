#str list tuple set dict range
'''
for var in seq:
   #stmts
   
s = 'python programin'
for i in s:
    print(i)
    --------------

l = [1,2,3,4,5]

for num in l:
    print(num)
    -----------------

prices = (9874,6547,523,225)
for price in prices:
    print(price)
    -------------------
    
names = {'eswar','lucky','vrdhan'}
for name in names:
    print(name)
    --------------------

d = {1:2,2:4,3:6,4:8,5:10}
for i in d:
    print(i,d[i])
    -------------------

range (start,end+1,step):(0,,1)

for i in range (1,11):
    print(i)
--------------
for i in range (5,101,5):
    print(i)
-----------

for i in range (5,0,-1):
    print(i)
    ---------------

s = 'R Programming'
for i in range(len(s)):
    print(i,s[i])
----------------------------

s = [456,1354,656,98,755,664,797]
for i in range(len(s)):
    print(i,s[i])
---------------------

s = {456,1233,789,456}
for i in enumerate(s):
    print(i[0],i[1])
    ------------------

d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
---------------------

for i in range (1,11):
    if i==5:
        break
    print(i)
    --------------

for i in range (50,77):
    if i==70:
        continue
    print(i)
------------------

for i in range (1,11):
    if i==15:
        break
    print(i)
else:
    print("End of the Loop")
----------------

l = [12,13,15,16,17,18,19]
n=19
for i in l:
    if i == n:
        print(n,"found")
        break
else:
    print(n,"not foud")
----------------
    
pin = 3777

for i in range(3):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Unlock Phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")
--------------------------------

n = 7
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
----------------
'''
    

