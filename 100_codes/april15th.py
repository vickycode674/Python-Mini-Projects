#factorial of a number dude

def factorial(n):
     if n==0 or n==1:
         return 1
     else:
         return n * factorial(n-1)
    

print("The factorial value of a number is",factorial())

#using itteartive method for factorial number

def factorial(n):
   value = 1  # Initialize value to 1, the multiplicative identity

   while n>0:
       value = value*n 
       n=n-1;
   return value
 
print("Here is the factorial of number==========",factorial(4))

# power of number 

num, power = 3, 2
# print(pow(num,power))

output = 1 

for i in range(power):
    output*=num  #running loop and running power times the respective number
    print(output)
    
print(num**power)


# finding factors of a number:

def factors(n):
    facto = []
    for i in range(1,n+1):
        if n%i==0:
            facto.append(i);
    return facto
    

print("Here are the factors of the number:", factors(10))

import math
 
def factors(n):
    facto=set()
    for i in range(1,int(math.sqrt(n))+1):
        if n%i ==0:
            facto.add(i)
            facto.add(n//i)
    return sorted(facto)

print("Here are the factors of the number:", factors(10))

    
   
            
