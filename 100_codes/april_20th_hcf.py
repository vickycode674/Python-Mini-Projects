# hcf

# euclieandean method fastest to solve 
def hcf_num(a,b):
    while b!=0:
        a,b = b ,a%b
    return a 



def hcf_num(a,b):
    for i in range(1,min(a,b)+1):
        if(a%i==0 and b%i==0):
           hcf = i
    return hcf


print("Here is the number hcf_num",hcf_num(60,120)) 
 
#  //lowest common multiple  [LCM] 

LCM = (a*b // hcf_num(a,b))  #here hcf is same as gcd its mainly to find the most common divosr for the given numebrs