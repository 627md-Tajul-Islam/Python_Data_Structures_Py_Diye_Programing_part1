def is_prime1(n):
    if n < 2:
        return False
    prime = True
    for x in range(2,n):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
    return

while True:
    number = input("Please enter a number (press 0 to exit): ")
    number = int(number)
