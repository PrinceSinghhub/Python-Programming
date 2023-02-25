n=int(input("enter the n"))
if n==1:
    for row in range (0,7):
     for col in range (0,5):
        if ((col==0 or col==4 ) and (row!=0) or (row==0 or row==3 ) and (col>0 and col<4)):
            print("*",end="")
        else:
           print(end=" ")
     print()
elif n==2:
    for row in range (0,7):
      for col in range (0,5):
         if ((col==0 or (col==4 and row!=3 and row!=6 and row!=0)) or (row==0   or row==3 or row==6) and (col>0 and col<4)):
           print("*", end="")            
         else:
           print(end=" ")
      print()  
elif n==3:
     for row in range (0,7):
       for col in range (6):
           if((col==0 ) and (row!=0 and row!=6) or (row==0   or  row==6) and (col>0 and col<5)):
                print("*", end="")            
           else:
            print(end=" ")
       print()  
elif n==4:
     for row in range (0,7):
       for col in range (7):
            if ((col == 2 or col == 6) and (row != 0 and row != 6) or (row == 0 or row == 6) and (col > 0 and col < 6)):
                print("*", end="")
            else:
                print(end=" ")
       print()
elif n==5:
    for row in range (0,7):
       for col in range (6):
           if((col==0 )  or (row==0 or row==6 or row==3) and (col>0 and col<5)):
                print("*", end="")            
           else:
            print(end=" ")
       print() 
elif n==6:
     for row in range (0,7):
       for col in range (6):
           if((col==0 )  or (row==0  or row==3) and (col>0 and col<5)):
                print("*", end="")            
           else:
            print(end=" ")
       print() 
     