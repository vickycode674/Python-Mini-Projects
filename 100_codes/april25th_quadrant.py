# python quadrants finding using coordinates..

coordinate1 = int(input("Enter X coordinate "))
coordinate2 = int(input("Enter Y Coordinate"))

def get_quadrant(coordinate1,coordinate2):
    if coordinate1 > 0 and coordinate2 >0:
        print("Its in Ist quadrant")
    elif coordinate1 >0 and coordinate2<0:
        print("Its in IVth")
    elif coordinate1<0 and coordinate2>0:
        print("Its in II")
    elif coordinate1<0 and coordinate2<0:
        print("Its in III")
    else:
        print("You have entered a either x or y as zero so it lies on the axies rather than quadrants dude..")
        

print("To check the working of quadrants here is the flow====",get_quadrant(coordinate1,coordinate2));


# //prime number rampage 
# prime number in range of 1 to 100: {Unforgettable question in history of vivek  sai 
import math
var = int(input("Enter a range of number to get prime in between them"))

def check_prime(value):
    for i in range(2,value-1): #we need to remember that we can let it #divisble itself so we need to make it less than that number
        if value%i==0:
            return False
    return True
    
def prime_in_range(var):
    li=[]
    for i in range(2,var+1):
        if check_prime(i):
            li.append(i)
    return li
    

print("Here is the Range of number between 1 and respective number========",prime_in_range(var));
            