def decimal_to_binary(decimal_number):
    lista = []
    while decimal_number > 0:
        result = decimal_number // 2
        mod = decimal_number % 2
        decimal_number = result
        lista.append(str(mod))
    print("".join(reversed(lista)))
        
#decimal_to_binary(120)

def binary_to_decimal(binary_digits):
    number = 0
    res = [int(x) for x in str(binary_digits)]
    res.reverse()
    for i in range(0, len(res), 1):
        calc = 2 ** i * res[i]
        number += calc
    print(number)

binary_to_decimal(1110001)

def binary_to_decimal2(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    y = 0
    binary_digits.reverse()
    for i in range(0, len(binary_digits),1):
        x = binary_digits[i] * 2 ** i
        y += x 
    return y
print(binary_to_decimal2([1, 1, 1, 1]))

def decimal_to_base(decimal_number, destination_base):
    pass

            
            
            