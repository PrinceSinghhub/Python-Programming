print("please insert card :")
a=int(input("enter the number between 27 and 80:\n"))
if 80<=a or a>=27:
    print("yes")
else:
    print("no your input is wrong try again later")
money =30000
code=5680
remove_money =int(input("enter the money 500 rupay maxium and less than 10000:"))
b=int(input("enter the your 4 digit code"))
if remove_money>=500 or 10000<=remove_money:
    print("the money 500 rupay maxium and less than 10000:")
if code==b:
    print("your transication successful")
    money-=remove_money
    print("remidir money your account:",money)
else:
    print("your pin is wrong please take card and try again:")
