year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("is a leap year")
else:
    print("is not a leap year")    





           
 
 
year=int(input())
if(year%100==0 and year%400==0):
   print("leap yr")
elif year%100!=0 and year%4==0:
    print("leap year")
else:
    print("not leap year")       

