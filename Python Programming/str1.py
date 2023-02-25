Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="Prince"
>>> x*2
'PrincePrince'
>>> a="Prince Singh"
>>> a[3]
'n'
>>> a[-3]
'n'
>>> z="Hellow"
>>> z[2:5]
'llo'
>>> z[:]
'Hellow'
>>> a="Prince Singh"
>>> a[2:12]
'ince Singh'
>>> a[0:12:2]
'Pic ig'
>>> a[0:12:4]
'Pci'
>>> a[-0:-12:2]
''
>>> a[-1:-12:-2]
'hnSenr'
>>> x="Hello"
>>> x[::-1]
SyntaxError: invalid syntax
>>> x[::-1]
'olleH'
>>> #+ and * operators
>>> x="Hello"
>>> y="Prince"
>>> z=x+y
>>> z
'HelloPrince'
>>> x*2
'HelloHello'
>>> #for loop with string
>>> for i in "Prince":
	print(i*2,end=" ")

	
PP rr ii nn cc ee 
>>> x.isalpha()
True
>>> x=10,20,30,20
>>> x.isdigit
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x.isdigit
AttributeError: 'tuple' object has no attribute 'isdigit'
>>> x='20.20'
>>> x.isdigit
<built-in method isdigit of str object at 0x03D4A360>
>>> a="123456"
>>> a.isdigit()
True
>>> z='20,10'
>>> z.isdigit()
False
>>> a="1,2,3"
>>> a.isdigit
<built-in method isdigit of str object at 0x03D4A3E0>
>>> a.digit()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.digit()
AttributeError: 'str' object has no attribute 'digit'
>>> a.isdigit()
False
>>> s="apple"
>>> s.islower()
True
>>> t="PRINCE@$"
>>> t.isupper()
True
>>> b="@#$"
>>> b.isupper()
False
>>> b.islower()
False
>>> h="Prince"
>>> h.lower()
'prince'
>>> g="PRINCE"
>>> g.lower()
'prince'
>>> j='prince'
>>> j.upper()
'PRINCE'
>>> h="                  abc"
>>> h
'                  abc'
>>> h.lstrip()
'abc'
>>> d="lmj320                         "
>>> d
'lmj320                         '
>>> d.rstrip()
'lmj320'
>>> t="Prince"
>>> ord("t")
116
>>> ord("t")
116
>>> ord('a')
97
>>> chr(97)
'a'
>>> 