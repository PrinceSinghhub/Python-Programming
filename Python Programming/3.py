Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={1,2,3}
>>> type(a)
<class 'set'>
>>> s={a:'appla', b:'boy'}
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s={a:'appla', b:'boy'}
NameError: name 'b' is not defined
>>> s={'a':'appla', 'b':'boy'}
>>> s
{'a': 'appla', 'b': 'boy'}
>>> type(s)
<class 'dict'>
>>> a={1:'a',2:'b'}
>>> type(a)
<class 'dict'>
>>> d={'name': 'P','a': '10'}
>>> type(a)
<class 'dict'>
>>> type(d)
<class 'dict'>
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87}
>>> m['alex']
45
>>> m={'alex': 45,'bob': 98,'chesf': 87,'bob':40}
>>> m
{'alex': 45, 'bob': 40, 'chesf': 87}
>>> m['bob']=60
>>> m
{'alex': 45, 'bob': 60, 'chesf': 87}
>>> m['prince']=100
>>> m
{'alex': 45, 'bob': 60, 'chesf': 87, 'prince': 100}
>>> del m['alex']
>>> m
{'bob': 60, 'chesf': 87, 'prince': 100}
>>> # itratting through a dictonary
>>> x={4:20,'yo':50,2:'apple'}
>>> for i in x:
	x[i]

	
20
50
'apple'
>>> #add to dicitonary
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> a={'alex': 45,'bob': 98,'chesf': 87}
>>> m['a']
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    m['a']
KeyError: 'a'
>>> m[a]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    m[a]
TypeError: unhashable type: 'dict'
>>> m['a']=m
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87, 'a': {...}}
>>> m['a']={'alex': 45,'bob': 98,'chesf': 87}
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87, 'a': {'alex': 45, 'bob': 98, 'chesf': 87}}
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> a={'a':30,'b':40,'c':50}
>>> m['a']={'a':30,'b':40,'c':50}
>>> a
{'a': 30, 'b': 40, 'c': 50}
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87, 'a': {'a': 30, 'b': 40, 'c': 50}}
>>> m['a']=a
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87, 'a': {'a': 30, 'b': 40, 'c': 50}}
>>> {'a':30,'b':40,'c':50}
{'a': 30, 'b': 40, 'c': 50}
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> p={'a':10,'b':20,'c':30}
>>> m['p']
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    m['p']
KeyError: 'p'
>>> m['p']=p
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87, 'p': {'a': 10, 'b': 20, 'c': 30}}
>>> a={'a':10,'b':20}
>>> a['c']=30
>>> a
{'a': 10, 'b': 20, 'c': 30}
>>> a['b']=30
>>> a
{'a': 10, 'b': 30, 'c': 30}
>>> a
{'a': 10, 'b': 30, 'c': 30}
>>> a.clear()
>>> a
{}
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> n=m.copy
>>> n
<built-in method copy of dict object at 0x031674D8>
>>> n=m.copy()
>>> n
{'alex': 45, 'bob': 98, 'chesf': 87}
>>> n['ram']=20
>>> n
{'alex': 45, 'bob': 98, 'chesf': 87, 'ram': 20}
>>> m
{'alex': 45, 'bob': 98, 'chesf': 87}
>>> z={1:2,2:3,3:4}
>>> a=z.items
>>> a
<built-in method items of dict object at 0x033D9F78>
>>> z
{1: 2, 2: 3, 3: 4}
>>> a=z.items()
>>> a
dict_items([(1, 2), (2, 3), (3, 4)])
>>> type(a)
<class 'dict_items'>
>>>  m={'alex': 45,'bob': 98,'chesf': 87}
 
SyntaxError: unexpected indent
>>> m={'alex': 45,'bob': 98,'chesf': 87}
>>> a=m.keys
>>> a
<built-in method keys of dict object at 0x033D98C0>
>>> a=m.keys()
>>> a
dict_keys(['alex', 'bob', 'chesf'])
>>> s=m.values()
>>> s
dict_values([45, 98, 87])
>>> a={1:2,2:3}
>>> a
{1: 2, 2: 3}
>>> b={3:4,4:5}
>>> b
{3: 4, 4: 5}
>>> c=a.update(b)
>>> c
>>> c
>>> a
{1: 2, 2: 3, 3: 4, 4: 5}
>>> a
{1: 2, 2: 3, 3: 4, 4: 5}
>>> a={1:2,2:3}
>>> b={3:4,4:5}
>>> a.update(b)
>>> a
{1: 2, 2: 3, 3: 4, 4: 5}
>>> z=a.update(a)
>>> print(z)
None
>>> z
>>> a
{1: 2, 2: 3, 3: 4, 4: 5}
>>> a={1:2}
>>> b={1:6}
>>> a.update(b)
>>> a
{1: 6}
>>> # bubble short
>>> a=[8,4,1,3,2,6]
>>> for i in range (len(a)):
	for j in range (1:len(a)):
		
SyntaxError: invalid syntax
>>> 