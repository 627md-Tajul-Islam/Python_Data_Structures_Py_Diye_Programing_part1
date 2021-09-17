def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2,n):
