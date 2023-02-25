n1 = int(input("Enter a First  Number"))
import math
e=math.e**n1
a = math.radians(n1)
sin=math.sin(a)
cos=math.cos(a)
tan=math.tan(a)
n = input("Select Operator")
if n1==0:
    print("log undifined")
elif n == 'log':
     log=math.log(n1)
     print(log)
elif n == '**0.5':
    print(n1**0.5)
elif n== 'e':
       print(e)
elif n== 'sin':
        print(sin)
elif n== 'cos':
        print(cos)
elif n== 'tan':
        print(tan)
else:
   n2 = int(input("Enter a Second Number"))
if n == '+':
        print(n1 + n2)
elif n == '-':
        print(n1 - n2)
elif n == '*':
        print(n1 * n2)
elif n == '/':
        print(n1 / n2)
elif n == '%':
      print(n1 % n2)
elif n == '**':
        print(n1 ** n2)



    
    