Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Python Operaters
# Arthamatic Operators
a=10
b=5
a+b
15
a-b
5
a*b
50
a/2
5.0
9/2
4.5
9//2
4
#Comparision Opearator
a
10
b
5
a<b
False
a>b
True
a<=b
False
a>=b
True
a == b
False
a!=b
True
#Assignment Operations
a = 20
a = a+10
a
30
a=a+20
a
50
a += 10
a
60
a -=10
a *=20
a
1000
a //= 2
a
500
a **= 2
a
250000
a /=500
a
500.0
a=100
a %= 3
a
1
a=+1
a
1
a+=1
a
2
#Relational Operator
email = True
password = False
eamil and password
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    eamil and password
NameError: name 'eamil' is not defined. Did you mean: 'email'?
email and password
False
login = True
login = False
display_products = True
login or display_products
True
's' in 'aeiou'
False
's' is not 'aeiou'
True
7%2==0 and 3%2==0
False
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==0
False
not 3%2==0
True
#Membership operators
#str,list,tuple,se,dict
s= 'python programming'
'python' in s
True
'java' in s
False
'z' in s
False
'a' in s
True
'c++' not in s
True
'program' not in s
False
1 = [1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l = [1,2,3,4]
3 in l
True
9 not in l
True
l not in 1
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    l not in 1
TypeError: argument of type 'int' is not a container or iterable
l not in 1
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l not in 1
TypeError: argument of type 'int' is not a container or iterable
l not in 1
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l not in 1
TypeError: argument of type 'int' is not a container or iterable
t = (20,30,40,50)
50 in t
True
3o not in t
SyntaxError: invalid decimal literal
30 not in t
False
s = {'pen','paper','book'}
'book' in s
True
'book' not in s
False
data = {'name':lucky,'batch':65,'course':'pfs'}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    data = {'name':lucky,'batch':65,'course':'pfs'}
NameError: name 'lucky' is not defined
data = {'name':'lucky','batch':65,'course':'pfs'}
'batch' in data
True
'age' not in data
True
'dob' in data
False
'lucky' in data
False
False
False
#Identity operators
l = [1,2,3,4]
m = [1,2,3,4]
id(l)
2118216415616
id(m)
2118216150912
l == m
True
i
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    i
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> l is m
False
>>> n = m
>>> n
[1, 2, 3, 4]
>>> id(n)
2118216150912
>>> m is n
True
>>> n is m
True
>>> n is l
False
>>> n is not l
True
>>> #Bitwise Operator
>>> 11 & 12
8
>>> 11 | 15
15
>>> 11 ^ 12
7
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 16>>2
4
>>> 2<<4
32
>>> ~14
-15
>>> ~78
-79
>>> ~23
-24
