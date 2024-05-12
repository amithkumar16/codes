sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
percent=float(((sub1+sub2+sub3+sub4+sub5)/500)*100)
#print("percent")
if(percent>=75):
    print("grade A")
elif(percent>=60 and percent<74):
    print("grade B")
elif(percent>=35 and percent<59):
    print("grade c")
else:
    print("fail") 
    
               