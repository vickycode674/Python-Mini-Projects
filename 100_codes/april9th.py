#1  finding out positive or negative number
# var =int(input("Enter a number to verify positive or negative:"))

# if var>0:
#     print("positive")

# else:
#     print("negative")


# # 2#2 Finding even or odd number

# var =int(input("Enter a number to verify even or odd:"))

# if var%2 ==0:
#     print("Even number")

# else:
#     print("Odd number")

# # 3 sum of n natuarl numbers

# n =int(input("Enter a number to verify sum of n natural numbers:"))

# if n > 0:
#     total = 0
#     for i in range(1,n+1):  #in python range begin from 0 to n-1 thats the reason we are adding in n
#         total +=i
#     print("Sum of n natural numbers is:", total)

#4 Sum of given numbers in a range using a fucntion

def sum_of_value(start,end):  #fucntion parameter to pass the values dude
     total = 0
     for i in range(start,end+1):
          total+=i
     return total #should be return out of the for loop

print(sum_of_value(1,5))

#5 Greatest of two numbers

def greatest_two(a,b):
    if a> b:
         return a
    else:
        return b
    
print("The greatest value between two integers is",greatest_two(10,20))


#6 Greatest of three numbers

def greatest_three(a,b,c):
  if a>b and a>c:
      return a
  elif b>c:
        return b
  else:
        return c
  
print(greatest_three(10,2,30))

#7 Leap year or not
def leap_year(year):
    if year%4 == 0 and  year%100!=0 and year%400==0:
        return True
    else:
        return False

#8 Checking prime number and its sum in range dude

import math

def checkPrime(a):
    if a<2:
        return False
    
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return False
        
    return True

var =int(input("Enter a number to check the prime number ra mava"))

sum_of_primes = 0
for i in range(var+1):
    if(checkPrime(i)):
        sum_of_primes = sum_of_primes+ i;
print(f"Here is the sum of prime numbers in the range 0 to {var-1} dude: {sum_of_primes}")

    
