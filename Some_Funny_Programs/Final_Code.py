import math

def is_prime5(n=1013):
    if n < 2:
        return False
    if n == 2:
        return
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3,m,2):
        return False
    return True
