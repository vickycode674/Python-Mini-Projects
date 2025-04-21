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
       n=n-1
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
            facto.append(i)
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

# april 16th
#finding prime factors of a number

var = int(input("Enter a number to get is prime factors of it"))
factors = []

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def prime_factor(n):
    for i in range(2,n):
        if n%i==0 and is_prime(i):
            factors.append(i)
    return factors
    
print(f"Here i the prime factors of {var} is========",prime_factor(var))

#Strong number: A Strong Number is a number where the sum of the factorials of its 
# digits equals the original number itself.

# strong number 

def facto(n):
    total=1
    while n>1:
        total=total*n
        n=n-1
    return total
    
    
def strong_number(n):
    temp=n
    value=0
    while temp>0:
        digit = temp%10
        value = value + facto(digit)
        temp=temp//10
    
    if n==value:
        print("Yes yes what you said is correct this is strong number",n,value)
    else:
        print("No No Its not a strong strong_number",n,value)

strong_number(145)

       

    
   
            
