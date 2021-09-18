def is_prime3(n):
    if n == 2:
        return True # 2 is prime
    if n % 2 == 0:
        print(n, "is divisible by 2")