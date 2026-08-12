Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#white space
s = '   Hello      World    '
s.strip()
'Hello      World'
s.lstrip()
'Hello      World    '
s.rstrip()
'   Hello      World'
s.replace(' ','')
'HelloWorld'
s = 'java-python-mysql-flask-fastpi-c'
s.plit('-')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.plit('-')
AttributeError: 'str' object has no attribute 'plit'. Did you mean: 'split'?
s.split('-')
['java', 'python', 'mysql', 'flask', 'fastpi', 'c']
s.split('-',2)
['java', 'python', 'mysql-flask-fastpi-c']
s.rsplit('-',2)
['java-python-mysql-flask', 'fastpi', 'c']
l = '''python'''
l = '''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c = ['python','java','mysql','flask']
c
['python', 'java', 'mysql', 'flask']
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
', '.join(c)
'python, java, mysql, flask'
'@'.join(c)
'python@java@mysql@flask'
'-'.join(('1','2','3',))
'1-2-3'
'-'.join({'1','2','3'})
'2-3-1'
a = 'strings.py'
a.partition9('.')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.partition9('.')
AttributeError: 'str' object has no attribute 'partition9'. Did you mean: 'partition'?
a.partition('.')
('strings', '.', 'py')
a.rpartition('-')
('', '', 'strings.py')
a = 'string.py.java.png.txt'
s
'java-python-mysql-flask-fastpi-c'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
#string testing method
a = 'strings.png'
a.strtswith('str')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.strtswith('str')
AttributeError: 'str' object has no attribute 'strtswith'. Did you mean: 'startswith'?
a.startswith('str')
True
a.startswith('list')
False
a.endswith('.py')
False
'pythonv.13'.islower()
True
>>> 'pythonv.13'.islower()
True
>>> 'Pythonv.13'.islower()
False
>>> 'PYTHON23456@#$%'.isupper()
True
>>> 'estyu'.isalpha()
True
>>> 'estyu8745'.isalpha()
False
>>> 'vgfdtgyfugdf'.isalnum()
True
>>> '987654'.isalnum()
True
>>> '       '.isspace()
True
>>> '     Hello'.isspace()
False
>>> 'Hlo  Wor'.isidentified()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    'Hlo  Wor'.isidentified()
AttributeError: 'str' object has no attribute 'isidentified'. Did you mean: 'isidentifier'?
>>> 'Hlo  Wor'.istitle()
True
>>> 'HLO Word'.istitle()
False
>>> 'my_var'.isidentified()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    'my_var'.isidentified()
AttributeError: 'str' object has no attribute 'isidentified'. Did you mean: 'isidentifier'?
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> '12345'.isdecimal()
True
>>> 'ERTYUIDFG'.isdecimal()
False
>>> '43567'.isdigit()
True
>>> '9876'.isnumeric()
True
