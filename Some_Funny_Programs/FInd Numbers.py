import random

number = random.randint(1,100)
attempts = 0

while True:
    input_number =  input("Guess between (1-100): ")
    input_number = int(input_number)
    attempts += 1

