import math

def square_root():
    num = float(input("Enter a number: "))

    if num < 0:
        print("Square root of a negative number is not possible.")
    else:
        result = math.sqrt(num)
        print("Square root =", result)

square_root()
