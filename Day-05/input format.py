Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float complex str list tuple set dict bool
a = input()
codegnan
a
'codegnan'
a = input()
2525
a
'2525'
a = input("Enter the Value: ")
Enter the Value: asdfghjkl77
a
'asdfghjkl77'
marks = input("Enter the marks:")
Enter the marks:70
marks
'70'
price = float(input("Enter the price:"))
Enter the price:12.65
price
12.65
cgpa = float(input("Enter the cgpa:"))
Enter the cgpa:7.2
cgpa
7.2
#input foe take list
names.split()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names=tuple(input.()split())
SyntaxError: invalid syntax
names=tuple(input().split())
ayaansh roni deva
names
('ayaansh', 'roni', 'deva')
names.split()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.split()
AttributeError: 'tuple' object has no attribute 'split'
names=tuple(input().split())
ayaansh roni deva
names
('ayaansh', 'roni', 'deva')
course='python-java-flask-css'
course.split('-')
['python', 'java', 'flask', 'css']
softskills='communication quicklearner'
softskills.split()
['communication', 'quicklearner']
names=input("enter the name: ").split()
enter the name: ayaansh roni deva
names
['ayaansh', 'roni', 'deva']
names=tuple(input("enter the names:").split())
enter the names:ayaash roni deva
names
('ayaash', 'roni', 'deva')
names=set(input("enter the names:").split())
enter the names:ayyansh roni deva
names
{'roni', 'deva', 'ayyansh'}
marks=input().split()
12 52 45 78 36
marks
['12', '52', '45', '78', '36']
map(int,marks)
<map object at 0x000001503BAC8680>
list(map(int,marks))
[12, 52, 45, 78, 36]
marks=list(map(int,input("enter the marks").split()))
enter the marks12 52 45 78 63 96
marks
[12, 52, 45, 78, 63, 96]
[12, 52, 45, 78, 63, 96]
[12, 52, 45, 78, 63, 96]
marks=tuple(map(int,input("enter the marks").split()))
enter the marks

52 12 3 66 36 36 35
SyntaxError: invalid syntax
25 12 78 63 35
SyntaxError: invalid syntax
45 10 23 25 26 35
SyntaxError: invalid syntax
45 25 65 35
SyntaxError: invalid syntax
>>> marks=tuple(map(int,input("enter the marks").split()))
enter the marks54 24 56 78
>>> marks
(54, 24, 56, 78)
>>> marks=set(map(int,input("enter the marks").split()))
enter the marks25 78 69 77
>>> marks
{25, 77, 69, 78}
>>> a,b=[1,2]
>>> a
1
>>> a
1
>>> b
2
>>> a,b,c
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a,b,c
NameError: name 'c' is not defined
>>> a,b
(1, 2)
>>> a,b,c=(1,12.2,3"str")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a,b,c=(1,12.2,3,"str")
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a,b,c=(1,12.2,3,"str")
ValueError: too many values to unpack (expected 3, got 4)
>>> a,b,c=(1,12.3,"str")
>>> a
1
>>> b
12.3
>>> c
'str'
>>> email,password=input("Enter the email,Password:").split()
Enter the email,Password:lucky@44 456
>>> email
'lucky@44'
>>> password
'456'
>>> name,marks=input("Enter the names and Marks:")
Enter the names and Marks:kushal 56
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    name,marks=input("Enter the names and Marks:")
ValueError: too many values to unpack (expected 2)
name,marks=input("Enter the names and Marks:").split()
Enter the names and Marks:kushal 85
name
'kushal'
marks
'85'
int(marks)
85
a,b,c=(list(map(int,input().split()))
       12 34 45
       
SyntaxError: '(' was never closed
a,b,c=(list(map(int,input().split())))
       
a,b,c=(list(map(int,input().split())))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a,b,c=(list(map(int,input().split())))
ValueError: invalid literal for int() with base 10: 'a,b,c=(list(map(int,input().split())))'
a,b,c=(list(map(int,input().split())))
       
a,b,c=(list(map(int,input().split())))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a,b,c=(list(map(int,input().split())))
ValueError: invalid literal for int() with base 10: 'a,b,c=(list(map(int,input().split())))'
a,b,c=(list(map(int,input().split())))
       

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a,b,c=(list(map(int,input().split())))
ValueError: not enough values to unpack (expected 3, got 0)
a,b,c=list(map(int,input().split()))
       

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 0)
a,b,c=list(map(int,input().split()))
       
a,b,c = list(map(int,input().split()))
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a,b,c=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'a,b,c'
a,b,c = list(map(int,input().split()))
       
132 23 34
a,b,c
       
(132, 23, 34)
a
                  
12
b
                  
13
c
                  
14
status = eval(input())
                  
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...                   
True
>>> status
...                   
True
>>> type(status)
...                   
<class 'bool'>
>>> status = eval(input())
...                   
[1,2,3,4]
>>> ststus = eval(input())
...                   
status = eval(input())
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    ststus = eval(input())
  File "<string>", line 1
    status = eval(input())
                  ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
>>> status = eval(input())
...                   
2+3j
>>> type(status)
...                   
<class 'complex'>
>>> status = eval(input())
...                   
{'ZIP', 'ZAP', 'VIP'}
>>> type(status)
...                   
<class 'set'>
>>> status = eval(input())
...                   
('12', 'jan', '15', 'Feb', '13', 'Nov')
>>> type(status)
...                   
<class 'tuple'>
>>> status = eval(input())
...                   
college
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    status = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'college' is not defined. Did you mean: 'College'?
>>> status = eval(input())
...                   
College
>>>      
... type(status)
...                   
<class 'str'>
