import random

number = random.randint(1,1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess between 1-1000: ")
    input_number = (low + high) // 2 # only integer version
    print("My guess is", input_number)
    attempts += 1