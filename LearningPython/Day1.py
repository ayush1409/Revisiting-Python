
#function to represent a number in different base
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
