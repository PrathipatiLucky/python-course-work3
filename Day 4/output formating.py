Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #utput formating
>>> a = 10
>>> b = 12.3
>>> c = 'codegnan'
>>> print(a,b,c)
10 12.3 codegnan
>>>  print("a=",a,"b",b"c",c)
...  
SyntaxError: unexpected indent
>>> print("a=",a,"b",b"c",c)
a= 10 b b'c' codegnan
>>>  print("a=",a,"b",b,"c",c)
...  
SyntaxError: unexpected indent
>>> print("a=",a,"b",b,"c",c)
a= 10 b 12.3 c codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 12.3 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=12.3c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
12.3
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	12.3	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='\n\n')
a=	10	b=	12.3	c=	codegnan

>>> print("a=",a,"b=",b,"c=",c,sep='\t',end='@')
... 
a=	10	b=	12.3	c=	codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
print('a=%d d=%f c=%s'(a,b.c))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('a=%d d=%f c=%s'(a,b.c))
AttributeError: 'float' object has no attribute 'c'
print('a=%d d=%f c=%s'(a,b,c))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print('a=%d d=%f c=%s'(a,b,c))
TypeError: 'str' object is not callable
print('a=%d b=%f c=%s'(a,b.c))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print('a=%d b=%f c=%s'(a,b.c))
AttributeError: 'float' object has no attribute 'c'
print('a=%d d=%f c=%s'%(a,b.c))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('a=%d d=%f c=%s'%(a,b.c))
AttributeError: 'float' object has no attribute 'c'
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=12.300000 c=codegnan
print('a={} b={} c={}'.format(a,b,c))
a=10 b=12.3 c=codegnan
print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=12.3 c=codegnan
print('a={2} b={0} c={1}'.format(a,b,c))
a=codegnan b=10 c=12.3
