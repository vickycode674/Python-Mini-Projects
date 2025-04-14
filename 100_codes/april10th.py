#we need to create a sum of digits of number in python 

var = int(input("Enter a number you want to find the sum"))

temp=var
value=0

while temp!=0:
    k = temp%10
    value = value + k
    temp=temp//10
    
print("here is the sum of digits====",value)

#reverse a number in python

var = int(input("Enter a number to reverse it"))
temp = 0

while var!=0:
    k=var%10
    temp=temp*10+k 
    var=var//10
    
print("here is reverseing of the number enterd ",temp)

# #palindrome number in python
var = int(input("Enter a number to reverse it"))
temp = 0
temp1=var

while temp1!=0:
    k=temp1%10
    temp=temp*10+k 
    temp1=temp1//10
    
    
if temp==var:
      print("The both var and temp are palindrome numebrs",var,temp)

else:
    print("There are not palindrome numbers dude",var,temp)

    

# amstrong number dude 
import math
var = int(input("Enter a number to reverse it"))
temp = 0
temp1=var
size = len(str(var))

while temp1!=0:
    k=temp1%10
    root=math.pow(k,size)
    temp=temp+root
    temp1=temp1//10
    
if(temp==var):
    print("It is an amstrong number")
else:
    print("It is  not a amstrong number buddy")


# sum of amstrong number in a range \
import math

def amstrong_number(var):
   temp = 0
   temp1=var
   size = len(str(var))

   while temp1!=0:
     k=temp1%10
     root=math.pow(k,size)
     temp=temp+root
     temp1=temp1//10
     
   return temp==var

      

var=int(input("Enter the range of values"));

for i in range(10,var+1):
    if amstrong_number(i):
        print(i)

   
    