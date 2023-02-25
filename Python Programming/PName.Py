for  row in range(0,30):
    for col in range(0,7):
        if ((col==1 )or (col==5  and (row==1 or row==5 or row==2 or row==3 or row==4 or row==1 or row==10 or row==11 or row==12or row==13 or row==14 or row==15 or row==16 or row==5 or row==6 or row==7 or row==8 or row==9) ) or (row==0  or row==15 or row==16 or row==1) and (col>0 and col<6)):
            print("GuruOP",end="")
        else:
            print(end="      ")
    print()