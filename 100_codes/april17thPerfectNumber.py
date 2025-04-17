# Question 1 Perfect number in python
# Its nothing but a sum of all its divisor excluding itself dude..
#welcome to  the world of python

var = int(input("Etner a number to find perfect or not"))

def perfect_num(n):
    # arr=[]
    value=0
    for i in range(1,n):
        if n%i==0:
            # arr.append(i)
            value=value+i
    if value==n:
        print(f"THE RESPECTIVE {var} is PERFECT NUMBER")
     
    else:
        print("This is not a perfect number")
     

perfect_num(var)

# perfect square 
# 🔁 Live Comparison Example (n = 10^6):

# Version	Time (approx)	Code Simplicity	Scales Well
# Your Version	Slower – needs ~1000 iterations	Easy	❌
# Fast Version	Instant (1 op)	Clean	✅ ✅ ✅

#welcome to  the world of python
#perfect square

var = int(input("Etner a number to find perfect or not"))
import math
def perfect_square(n):
    # arr=[]
    flag=False
    # root = int(math.sqrt(n))
    # if root*root ==n:
    for i in range(1,n):
        if i*i==n:
            flag=True;
    if flag==True:
        print("perfect_square")
    else:
        print("Not a perfect_square")
    

perfect_square(var);
    
