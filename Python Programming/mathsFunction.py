n1 = int(input("Enter a First  Number"))
n = input("Select Operator")
import math
if n1==0:
    print("log undifined")
else:
    log=math.log(n1)
    print(log)
e=math.e**n1
a = math.radians(n1)
sin=math.sin(a)
cos=math.cos(a)
tan=math.tan(a)
if n == '**0.5':
    print(n1**0.5)

elif n== 'e':
    print(e)
elif n== 'sin':
        print(sin)
elif n== 'cos':
        print(cos)
elif n== 'tan':
        print(tan)
    

    
   
