Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Data Types
>>> #int float complex
>>> a = 12
>>> type(a)
<class 'int'>
>>> b = 13.4
>>> typae(b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    typae(b)
NameError: name 'typae' is not defined. Did you mean: 'type'?
>>> type(b)
<class 'float'>
>>> c = 12+4j
>>> type(c)
<class 'complex'>
>>> c = 12+6J
>>> c
(12+6j)
>>> #str list couple
>>> s = 'Codegnan'
>>> id(s)
2315168555440
>>> s += 'Python'
>>> s
'CodegnanPython'
>>> s = 'aaaaaaaaaaa'
>>> s
'aaaaaaaaaaa'
>>> type(s)
<class 'str'>
>>> l = [1,2,3,4,5,6]
>>> type(l)
<class 'list'>
>>> id(l)
2315168553600
>>> l.append(12)
[1, 2, 3, 4, 5, 6, 12]

id{l}
SyntaxError: invalid syntax
id(l)
2315168553600
l = [1,12,3,"str",[1,23]]
l
[1, 12, 3, 'str', [1, 23]]
type(l)
<class 'list'>
t=(1,2,3,45)
type(t)
<class 'tuple'>
t
(1, 2, 3, 45)
t=(1,21,3,4,"c")
t
(1, 21, 3, 4, 'c')
# set disct
s= (1,12,1,34,56,78,87,78,78,78)
s
(1, 12, 1, 34, 56, 78, 87, 78, 78, 78)
# set dict
s= {80,70,45,14,25,78,78,78,78}
s
{80, 70, 14, 25, 45, 78}
is(s)
SyntaxError: invalid syntax
id(s)
2315168063424
s.add(20)
s
{80, 20, 70, 14, 25, 45, 78}
