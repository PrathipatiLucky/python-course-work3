Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #data types
>>> #Iint, Float,complex
>>> a =12
>>> type(a)
<class 'int'>
>>> b = 13.4
>>> type(b)
<class 'float'>
>>> c=12+4j
>>> type(c)
<class 'complex'>
>>> #str, list, Tuple
>>> s = 'Codegnan'
>>> id(s)
2248024177136
>>> s +='Python'
>>> s
'CodegnanPython'
>>> id(s)
2247981762288
>>> s = 'aaaaaaa'
>>> type(s)
<class 'str'>
>>> #list is collecion of elements enclosed blw '[]'. list is mutable.list allows duplicates, dynamically shapes, allows heterogenous datatypes. It is also Ordered.
>>> l = [1,2,3,4,5,5,6,]
>>> type(l)
<class 'list'>
>>> id(1)
140729281922168
>>> l.append(12)
>>> l
[1, 2, 3, 4, 5, 5, 6, 12]
>>> id(1)
140729281922168
>>> l = [1,12.3, 'str', [1,23]]
>>> l
[1, 12.3, 'str', [1, 23]]
>>> #Tuple is a collection of object enclosed '<>'.
>>> t = (l,l,l,l,l)
>>> t
([1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]], [1, 12.3, 'str', [1, 23]])
>>> t=(1,1,1,1)
t
(1, 1, 1, 1)
t =( 1, 1.5, 'Number')
t
(1, 1.5, 'Number')
#set is a collection elements enclosed between '{}'.
a={ 1,12.3, "set"}
a
{1, 'set', 12.3}
se = {80, 20, 70, 14, 24,25, 78}
id(se)
2248023744672
se
{80, 20, 70, 25, 24, 78, 14}
#frozenset: A set which is not Mutable.
t = frozenset(["Fare", "Well"])
t
frozenset({'Fare', 'Well'})
frozenset({'Well', 'Fare'})
frozenset({'Fare', 'Well'})
type(t)
<class 'frozenset'>
#dictionary is the collection Key and value pairs.
student = {"name": "Rohit","age": 21,"course": "Python"}
student
{'name': 'Rohit', 'age': 21, 'course': 'Python'}
type(student)
<class 'dict'>
E = { "name" : "java","workingdays" : 45,"assement": "grandtest"}
E
{'name': 'java', 'workingdays': 45, 'assement': 'grandtest'}
#Boolean is is variable which only works with True or false or 0 and 1.
Log_in = true
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Log_in = true
NameError: name 'true' is not defined. Did you mean: 'True'?
log
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    log
NameError: name 'log' is not defined
-
log_in=true
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    log_in=true
NameError: name 'true' is not defined. Did you mean: 'True'?
log in = true
SyntaxError: invalid syntax
type(log in)
SyntaxError: invalid syntax
