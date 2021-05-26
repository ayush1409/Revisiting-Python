# WORKING WITH INTEGERS
# n = b * (n // b) + n % b
# Function to represent a number in different base
def from_bas_10(n, b):
    if b < 2:
        ValueError('base must be >= 2')
    if n < 0:
        ValueError('Number n must be positive')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, m = n // b, n % b
        digits.insert(0, m)
    return digits


# Encoding function
def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('Digit map is not long enough to encode digits')
    return ''.join(digit_map[d] for d in digits)


# Base conversion function
def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        ValueError('Invalid Base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_bas_10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


print(rebase_from10(10, 2))
