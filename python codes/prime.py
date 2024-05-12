

"""find the prime number between two numbers"""
def isprime(n):
    for i in range(2,n):
       if n%i==0:
        return False
    else:
        return True
a=int(input())
b=int(input())
for i in range(a,b+1):
        if isprime(i):
           print(i)
           
        
"""find prime 
n=int(input())
for i in range(2,n):
    if n%i==0:
        print(" not prime no")
        break
else:
    print("prime")"""

      