import math

def is_prime4(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False