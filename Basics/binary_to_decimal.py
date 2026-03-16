def binary_to_decimal_brute_force(binary_string):
    decimal_number = 0;
    power = 1
    
    for i in range(len(binary_string) - 1, -1, -1):
        count = int(binary_string[i])

        if count == 1:
            decimal_number += power
        
        power *= 2
        
    return decimal_number
    
print(binary_to_decimal_brute_force("1100"))
