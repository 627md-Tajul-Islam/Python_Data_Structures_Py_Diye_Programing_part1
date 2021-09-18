def is_prime3(n):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False # all even number except 2 are not prime

    if n < 2:
        return False # numbers less than 2 are not prime
    prime = True
    for x in range(3,n,2):
