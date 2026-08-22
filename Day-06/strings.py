Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string
#string operations : 1 cancatenation, indexing, slicing.
S = 'Codegnan'
S
'Codegnan'
# cancatenation
a= 'Python'
b= 'Programming'
a+b
'PythonProgramming'
a*10
'PythonPythonPythonPythonPythonPythonPythonPythonPythonPython'
type(S)
<class 'str'>
s = 'codegnan'
s
'codegnan'
s[5]
'n'
s[-8]
'c'
s[-5]
'e'
Names = "lucky vardan eswar kishorebabu sudarsan"
Names
'lucky vardan eswar kishorebabu sudarsan'
Names[:8]
'lucky va'
Names[:7]
'lucky v'
Names[8:11]
'rda'
Names[:9]
'lucky var'
Names[:17]
'lucky vardan eswa'
Names[-7:]
'udarsan'
#membership operations
'a' in Names
True
'y'in Names
True
'z' in Names
False
'Teja' not in Names
True
#String methods
len(Names)
39
ord('a)
    
SyntaxError: unterminated string literal (detected at line 1)
otd('a')
    
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    otd('a')
NameError: name 'otd' is not defined. Did you mean: 'ord'?
ord('a')
    
97
ord('e')
    
101
ord('i')
    
105
chr(100)
    
'd'
char(n)
    
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    char(n)
NameError: name 'char' is not defined. Did you mean: 'chr'?
>>> sorted(Names)
...     
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'd', 'd', 'e', 'e', 'h', 'i', 'k', 'k', 'l', 'n', 'n', 'o', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 'u', 'u', 'u', 'v', 'w', 'y']
>>> max(Names)
...     
'y'
>>> min(names)
...     
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    min(names)
NameError: name 'names' is not defined. Did you mean: 'Names'?
>>> min(Names)
...     
' '
>>> #Case conversion Methods
...     
>>> s= 'python Programming Languge'
...     
>>> s.upper()
...     
'PYTHON PROGRAMMING LANGUGE'
>>> s.lower()
...     
'python programming languge'
>>> s.title()
...     
'Python Programming Languge'
>>> s.capitalize()
...     
'Python programming languge'
>>> #alignment Methods
...     
>>> s
...     
'python Programming Languge'
>>> s.center(50,"-")
...     
'------------python Programming Languge------------'
>>> s.ljust(50,"-")
...     
'python Programming Languge------------------------'
