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

    if input_number == number:
        print("Its Correct")
        break
    if input_number > number:
        print("Incorrect, give a smaller number")
        high = input_number - 1
    else:
        print("Incorrect,give a bigger number")
        low = input_number + 1

print("You tried", attempts, "times to find the correct number")
# its working man