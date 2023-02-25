Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=20
>>> y=10
>>> n=x-=y
SyntaxError: invalid syntax
>>> x-=y
>>> x
10
>>> x*=y
>>> x
100
>>> a=10
>>> b=5
>>> a*=b
>>> a
50
>>> a/=b
>>> a
10.0
>>> a=10
>>> b=5
>>> a/=b
>>> a
2.0
>>> r=7
>>> 
>>> r=2
>>> r=7
>>> a=2
>>> r%=a
>>> r
1
>>> r=%a
SyntaxError: invalid syntax
>>> a=5
>>> b=2
>>> a//=b
>>> a
2
>>> a=5
>>> b=2
>>> a**=b
>>> a
25
>>> #relation oberator
>>> a=10
>>> b=5
>>> a==b
False
>>> a=5
>>> b=5
>>> a==b
True
>>> a=10
>>> b=5
>>> a!=b
True
>>> a=5
>>> b=5
>>> a!=b
False
>>> a=!b
SyntaxError: invalid syntax
>>> a=5
>>> b=2
>>> a>b
True
>>> a=2
>>> b=20
>>> a>b
False
>>> a=10
>>> b=5
>>> a>=b
True
>>> a=10
>>> b=10
>>> a>=b
True
>>> a=2
>>> b=10
>>> a>=b
False
>>> a=5
>>> b=10
>>> a<=b
True
>>> a=6
>>> b=10
>>> a>5 and b<12
True
>>> a>5 and b>10
False
>>> a=10
>>> b=5
>>> a<b or a>b
True
>>> a>b or b<a
True
>>> a<b or b>a
False
>>> a=10
>>> b=5
>>> not a>b
False
>>> not a<b
True
>>> #input()
>>> n=int(input("ni"))
ni
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    n=int(input("ni"))
ValueError: invalid literal for int() with base 10: ''
>>> a=5e-3
>>> a
0.005
>>> b=10e10
>>> b
100000000000.0
>>> a=1<10
>>> a
True
>>> b=1>10
>>> b
False
>>> a=6
>>> a
6
>>> a =5 and 6
>>> a
6
>>> a=5%2
>>> a
1
>>> a=7//2
>>> a
3
>>> a=2**2
>>> a
4
>>> a=10
>>> b=20
>>> a+=b
>>> a
30
>>> 