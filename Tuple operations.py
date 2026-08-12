Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
t = ()
t =tuple()
t = (1,2,3,45)
t
(1, 2, 3, 45)
t = (1)
t
1
t =(1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t=(1,23,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2,},True)
t
(1, 23, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>
t
(1, 23, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 23, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23
1[-1]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    1[-1]
TypeError: 'int' object is not subscriptable
t[-1]
True
t[-3]
{1, 2, 3}
t[2]
'str'
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t
(1, 23, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
23 in t
True
"str" in t
True
True in t
True
false in t
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    false in t
NameError: name 'false' is not defined. Did you mean: 'False'?
False in t
False
t = (12,34,789,65,258,654,1321,1735,32,45)
t
(12, 34, 789, 65, 258, 654, 1321, 1735, 32, 45)
max(t)
1735
min(t)
12
len(t)
10
t
(12, 34, 789, 65, 258, 654, 1321, 1735, 32, 45)
t.index(32)
8
t.index(1321)
6
t.count(45)
1
all((1,2,3))
True
any((1,2,3,00,0))
True
all({1,2,3,00,0))
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
all({1,2,3,00,0])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
all({1,2,3,00,0})
False
t = (1,2,3,4[1,2,3],5)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t = (1,2,3,4[1,2,3],5)
TypeError: 'int' object is not subscriptable
t = (1,2,3,4,[1,2,3],5)
t
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
[1, 2, 3]
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t=(1,2,34,4)
sum(t)
41
#mutable unorder
s=set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,132145,125,46546851,303}
s
{1, 2, 3, 4, 5, 6, 46546851, 303, 132145, 125}
s = (1,1,1,1,1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
s = {1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(12.3)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add9{1:1})
SyntaxError: unmatched ')'
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.add({1:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(Flase)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.add(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
s.add(False)
s
{False, 1, 12.3, 'str'}
a ={1,2,3,4,5}
b ={3,5,7,8,9}
2 in a
True
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
b - a
{8, 9, 7}
a =({1,2,4,6,7,8,9})
a
{1, 2, 4, 6, 7, 8, 9}
a=({1,2,3,4,5})
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3}{1,2,3,4}
{1,7,8,9}<=a
False
a>={1,2}
True
a>{15,16}
False
m={1,2,3}
n={4,5,6}
n.isdisjont(m)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    n.isdisjont(m)
AttributeError: 'set' object has no attribute 'isdisjont'. Did you mean: 'isdisjoint'?
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a = {12,43,1,7,89, 40 ,23,44}
a
{1, 7, 40, 43, 12, 44, 23, 89}
sorted(a)
[1, 7, 12, 23, 40, 43, 44, 89]
max a
SyntaxError: invalid syntax
max (a)
89
min(a)
1
len(a)
8
all
<built-in function all>
all({1,1,23,43,13,1})
True
any({0,''})
False
any({0,''})
False
any({0,"Str"})
True
a
{1, 7, 40, 43, 12, 44, 23, 89}
>>> a={1,2,3}
>>> b = a
>>> c a.copy()
SyntaxError: invalid syntax
>>> c = a.copy()
>>> c
{1, 2, 3}
>>> c.add(5)
>>> c
{1, 2, 3, 5}
>>> a
{1, 2, 3}
>>> a.add95)
SyntaxError: unmatched ')'
>>> a
{1, 2, 3}
>>> a.dd(5)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.dd(5)
AttributeError: 'set' object has no attribute 'dd'. Did you mean: 'add'?
>>> a.add(5)
>>> a
{1, 2, 3, 5}
>>> a.add(100)
>>> a
{1, 2, 3, 100, 5}
>>> a.add(40)
>>> a
{1, 2, 3, 100, 5, 40}
>>> a.update({10,20,30,40})
>>> a
{1, 2, 3, 100, 5, 40, 10, 20, 30}
>>> a.pop()
1
>>> a
{2, 3, 100, 5, 40, 10, 20, 30}
>>> a.remove(100)
>>> a
{2, 3, 5, 40, 10, 20, 30}
>>> a
{2, 3, 5, 40, 10, 20, 30}
>>> a.discard(10)
>>> a.discard(30)
>>> a
{2, 3, 5, 40, 20}
