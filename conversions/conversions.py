#decimal number to octal conversion
decimal_number = int(input("Enter any number for conversion:"))

def decimal_to_octal(N):
    if N == 0:
        return "0"
    
    octal_result = ""
    
    while N > 0:
        remainder = N % 8
        octal_result = str(remainder) + octal_result
        N //= 8
        
    return octal_result

print("Octal:", decimal_to_octal(decimal_number))

#octal to decimal conversion
octal_number = int(input("Enter the number to convert:"))

def octal_to_decimal(N):
    decimal_result = 0
    position = 0
    
    if N == 0:
        return "0"
    
    result_octal = ""
    
    while N > 0:
        digit = N % 10
        decimal_result += digit * (8 ** position)
        N //= 10
        position +=1
    
    return decimal_result
print("Decimal:", octal_to_decimal(octal_number))

#hexadecimal to decimal conversion
hexadecimal_number = input("Enter the number to convert: ")

def hex_to_decimal(N):
    decimal_result = 0
    position = 0
    hex_digits = '0123456789ABCDEF'
    N = N.upper()
    
    for digit in N:
        value  = hex_digits.index(digit)
        decimal_result = decimal_result * 16 +value
        
    return decimal_result

print("Hex_decimal:", hex_to_decimal(hexadecimal_number))

#decimal to binary conversion in different way
decimal_number = int(input("Enter the decimal number: "))

def decimal_to_binary(N):
    if N == 0:
        return "0"
    
    binary_string = " "
    
    while N > 0:
        remainder = N % 2
        binary_string = str(remainder) + binary_string
        N //= 2
        
    return binary_string

print("Binary:", decimal_to_binary(decimal_number))
