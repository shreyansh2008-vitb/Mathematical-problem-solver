import random

def random_number_generator():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > end:
        print("Starting number must be less than or equal to ending number.")
    else:
        number = random.randint(start, end)
        print("Random number =", number)

random_number_generator()
