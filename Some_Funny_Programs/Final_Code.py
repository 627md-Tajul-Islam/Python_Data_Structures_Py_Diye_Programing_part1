import math

def is_prime5(n=1013):
    if n < 2:
        return False
    if n == 2:
        return
    if n % 2 == 0:
        return False