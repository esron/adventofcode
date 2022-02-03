input  = 'D2FE28'

def hex_to_bin(input: str) -> str:
    """Convert from hex string to binary string"""
    return '{0:b}'.format(int(input, 16))

bin_string = hex_to_bin(input)

print(bin_string)
V = bin_string[:3]
print(V)
T = bin_string[3:6]
print(T)
