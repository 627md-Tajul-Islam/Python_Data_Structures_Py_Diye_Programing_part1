import random

number = random.randint(1,100)
attempts = 0

while True:
    input_number =  input("Guess between (1-100): ")
    input_number = int(input_number)
    attempts += 1

    if input_number == number:
        print("Its Correct")
        break
    if input_number > number:
        print