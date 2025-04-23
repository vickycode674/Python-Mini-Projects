decimal = 23
binary = bin(decimal)   # Returns '0b10111'
print("Binary:", binary[2:])  # Removing '0b' prefix

decimal = 23
octal = oct(decimal)  # Returns '0o27'
print("Octal:", octal[2:])  # Removing '0o' prefix


decimal = 23
hexa = hex(decimal)  # Returns '0x17'
print("Hexadecimal:", hexa[2:].upper())  # Removing '0x' and uppercase


def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

print("Binary of 23:", decimal_to_binary(23))


def decimal_to_octal(n):
    octal = ""
    while n > 0:
        remainder = n % 8
        octal = str(remainder) + octal
        n = n // 8
    return octal

print("Octal of 23:", decimal_to_octal(23))


def decimal_to_hex(n):
    hex_chars = "0123456789ABCDEF"
    hexa = ""
    while n > 0:
        remainder = n % 16
        hexa = hex_chars[remainder] + hexa
        n = n // 16
    return hexa

print("Hexadecimal of 23:", decimal_to_hex(23))


# binary to octal 
def binary_to_octal(binary_string):
    """Converts a binary string to its octal representation.

    Args:
        binary_string: The binary string (e.g., "1011001").

    Returns:
        The octal string representation (e.g., "131").
        Returns an empty string if the input is not a valid binary string.
    """
    try:
        # Convert binary string to an integer (base 2)
        decimal_value = int(binary_string, 2)
        # Convert the integer to its octal representation (returns a string with "0o" prefix)
        octal_value = oct(decimal_value)
        # Remove the "0o" prefix
        return octal_value[2:]
    except ValueError:
        return ""

# Example usage:
binary_num = "1011001"
octal_num = binary_to_octal(binary_num)
if octal_num:
    print(f"Binary: {binary_num} -> Octal: {octal_num}")
else:
    print(f"Invalid binary input: {binary_num}")

binary_num_invalid = "10120"
octal_num_invalid = binary_to_octal(binary_num_invalid)
if octal_num_invalid:
    print(f"Binary: {binary_num_invalid} -> Octal: {octal_num_invalid}")
else:
    print(f"Invalid binary input: {binary_num_invalid}")

    # octal to binary 
    def octal_to_binary(octal_string):
    """Converts an octal string to its binary representation.

    Args:
        octal_string: The octal string (e.g., "131").

    Returns:
        The binary string representation (e.g., "1011001").
        Returns an empty string if the input is not a valid octal string.
    """
    try:
        # Convert octal string to an integer (base 8)
        decimal_value = int(octal_string, 8)
        # Convert the integer to its binary representation (returns a string with "0b" prefix)
        binary_value = bin(decimal_value)
        # Remove the "0b" prefix
        return binary_value[2:]
    except ValueError:
        return ""

# Example usage:
octal_num = "131"
binary_num = octal_to_binary(octal_num)
if binary_num:
    print(f"Octal: {octal_num} -> Binary: {binary_num}")
else:
    print(f"Invalid octal input: {octal_num}")

octal_num_invalid = "189"
binary_num_invalid = octal_to_binary(octal_num_invalid)
if binary_num_invalid:
    print(f"Octal: {octal_num_invalid} -> Binary: {binary_num_invalid}")
else:
    print(f"Invalid octal input: {octal_num_invalid}")