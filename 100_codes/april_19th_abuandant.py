#abaundant number dude
# sum of the diviosrs is greter than actual given number 
# Sum of proper divisors > number.
# Ex: 12 → 1+2+3+4+6 = 16 > 12 ✅

var = int(input("Enter a number to check abaundant"))

def abaundant_num(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total=total+i 
    if total >=n:
        print("Its an abaundant number dude")
    else:
        print("its not an abaundant number rey")
        
abaundant_num(var)
        
# Mowa friendly pair ante superrr fun concept rey! 🔁✨

# 💡 Friendly Pair (also called amicable pair sometimes):
# Two numbers are friendly (or form a friendly pair) if:

# (Sum of divisors of A) / A == (Sum of divisors of B) / B

# This ratio is called the abundancy index.



# Friendly pair 

# Pair of numbers with same abundance ratio (sum of divisors / number).

# Example: (220, 284)

var1 = int(input("oka  nachina number enter cheyi mowa: "))
var2 = int(input("mee friend number enter cheyi mowa: "))

def friendly_pair(n1,n2):
    total1=0
    total2=0
    for i in range(1,n1):
        if n1%i==0:
            total1=total1+i 
    total1=total1/n1
    
    for i in range(1,n2):
        if n2%i==0:
            total2=total2+i 
    total2=total2/n2
    
    if total1==total2:
        print("Dost mera dost tu hi mera jaaan eyy ")
    else:
        print("Elehehy bengay evadra niku friendu")
    
        
friendly_pair(var1,var2)
        
