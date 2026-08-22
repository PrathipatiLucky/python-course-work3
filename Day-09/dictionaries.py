Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict : is mutable,order,hetro,dynamic,unidu
d={}
type(d)
<class 'dict'>
d = {1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d ={}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,4)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[[1:1,2:2,2]]=1
SyntaxError: invalid syntax
#as dict is heterogeneous but the key doesn't allow mutable
#values
d[1]
1
d[1]=1
d[2]=12.4
d[3]='str'
d[4]=2+j3
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[4]=2+j3
NameError: name 'j3' is not defined
d[4]=2+3j
d[5]=True
d[6]=[1,2,3]
d[7]=(1,3,45,6)
d[8]{1,2,3,4}
SyntaxError: invalid syntax
d[8]={1,2,3,4}
d[9]=[1:2,3:4,5:6]
SyntaxError: invalid syntax
d[9]=[1:2,3:4,5:6
      
SyntaxError: invalid syntax



d[9]={1:2,3:4,5:6}
      
d
      
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
#duplicates values allowed in keys
      

d[1]=3
      
d
      
{1: 3, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
d[1]=146
      
d
      
{1: 146, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}}
#keys should be unique,duplicate allowed for keys
      
d[10]=True
      
d
      
{1: 146, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}, 10: True}
d[10]=None
      
d
      
{1: 146, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}, 10: None}
{1: 146, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}, 10: None}
      
{1: 146, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 2: 12.4, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 3, 45, 6), 8: {1, 2, 3, 4}, 9: {1: 2, 3: 4, 5: 6}, 10: None}
d=
      
SyntaxError: invalid syntax

d={"name":"dinesh","course":"pfs",'batch':65}
      
d
      
{'name': 'dinesh', 'course': 'pfs', 'batch': 65}
#we can only perform membership
      
"dinesh" in d
      
False
"name" in d
      
True
#membership only works on keys
      
d.get('name')
      
'dinesh'
d['age']=21
      
d
      
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'age': 21}
#no error return
      
d.get('phone','9876543219')
      
'9876543219'
d.update({"email":"lucky77@gmail.com","git":"yes"})
      
d
      
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'lucky77@gmail.com', 'git': 'yes'}
id(d)
      
2706304440640
d['py']=2026
      
d
      
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'lucky77@gmail.com', 'git': 'yes', 'py': 2026}
id(d)
      
2706304440640
d['py']=2027
      
d
      
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'age': 21, 'email': 'lucky77@gmail.com', 'git': 'yes', 'py': 2027}
#delete a key we use pop()
...       
>>> d,popitem()
...       
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d,popitem()
NameError: name 'popitem' is not defined
>>> d.popitem()
...       
('py', 2027)
>>> del d["age']
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> del d ["age"]
...       
>>> d
...       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'email': 'lucky77@gmail.com', 'git': 'yes'}
>>> d.clear()
...       
>>> d
...       
{}
>>> {'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'email': 'lucky77@gmail.com', 'git': 'yes'}
...       
{'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'email': 'lucky77@gmail.com', 'git': 'yes'}
>>> d = {'name': 'dinesh', 'course': 'pfs', 'batch': 65, 'email': 'lucky77@gmail.com', 'git': 'yes'}
...       
>>> len(d)
...       
5
>>> d.keys()
...       
dict_keys(['name', 'course', 'batch', 'email', 'git'])
>>> d.items()
...       
dict_items([('name', 'dinesh'), ('course', 'pfs'), ('batch', 65), ('email', 'lucky77@gmail.com'), ('git', 'yes')])
>>> d.values()
...       
dict_values(['dinesh', 'pfs', 65, 'lucky77@gmail.com', 'yes'])
>>> d.get("clg":"NEC")
...       
SyntaxError: invalid syntax
>>> d.get("clg","NEC")
...       
'NEC'
