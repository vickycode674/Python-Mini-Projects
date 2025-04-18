# autmorphic_number with maths way
# THE SQUARE OF THE NUMBER ENDS WITH VALUES WILL BE EQUAL TO NUMBER DUDE 

var = int(input("Enter a number to autmorphic or not"))

def autmorphic_num(num):
    square = num*num
    temp =num
    
    while temp!=0:
        if(temp%10!=square%10):
            return false
        temp=temp//10
        square=temp//1
    return True
    
    

if autmorphic_num(var):
    print("Automorphic number ✅")
else:
    print("Not an Automorphic number ❌")

#string way 

var = int(input("Enter a number to autmorphic or not"))

def autmorphic_num(num):
    square = num*num
    str_num=str(num)
    str_square=str(square)
    
    if str_square.endswith(str_square):
        print("Automorphic number")
    else:
        print("Not an Automorphic number ❌")


autmorphic_num(var)

# harshad mawa number  
# ✅ Definition: Harshad Number
# A number is called a Harshad Number (also known as a Niven Number) if it is divisible by the sum of its digits.
var = int(input("Enter a number to Harshad or niven or not"))

def Harshad_num(var):
    
    temp=var
    value=0
    flag=0
    while temp!=0:
        
        last_digit=temp%10
        value=value+last_digit
        temp=temp//10
         
    if var%value==0:
        flag=1
     

    if flag ==0:
        print("This is an not Harshad_num")
    else:
        print("This is an Harshad_num");
Harshad_num(var)