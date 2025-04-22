# CONVERSTION OF BINARY TO DECIMA INTERGERS DUDE 

def binary_to_dec(var):
    binary_str= str(var)
    decimal_value = 0
    power = 0
    
    for i in reversed(binary_str):
        if i == '1':
            decimal_value = decimal_value + 2**power;
        power = power + 1
    return decimal_value
    
print("Here is the value of decimal dude =======",binary_to_dec(1011));

binary_input = "1011"
decimal_value = int(binary_input,2);
print("Heres is teh value========",decimal_value);

#Conversion of octal to Decimal number dude 

def octal_to_dec(var):
    binary_str= str(var)
    decimal_value = 0
    power = 0
    
    for i in reversed(binary_str):
        if i == '1':
            decimal_value = decimal_value + 8**power;
        power = power + 1
    return decimal_value
    
print("Here is the value of decimal dude =======",binary_to_dec(1011)); 

# 157 --> 111
 

 #  CONVERSTION OF HEX TO DECIMAL DUDE
 def hex_to_decimal(hex_str):
    return int(hex_str, 16)

print("Decimal value is:", hex_to_decimal("2F"))  # Output: 47


def hex_to_decimal(hex_str):
    hex_digits = '0123456789ABCDEF'
    hex_str = hex_str.upper()
    decimal_value = 0
    power = 0

    for char in reversed(hex_str):
        value = hex_digits.index(char)
        decimal_value += value * (16 ** power)
        power += 1

    return decimal_value

print("Decimal value is:", hex_to_decimal("2F"))  # Output: 47
