import square_root
import gcd
import divisor
import prime_generator
import prime_factorization
import fibonacci
import power
import random_number

while True:
    print("\n===== MATHEMATICAL PROBLEM SOLVER =====")
    print("1. Square Root Calculator")
    print("2. GCD Calculator")
    print("3. Smallest Divisor Finder")
    print("4. Prime Number Generator")
    print("5. Prime Factorization")
    print("6. Fibonacci Series")
    print("7. Power Calculator")
    print("8. Random Number Generator")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        square_root.square_root()
    elif choice == "2":
        gcd.gcd_calculator()
    elif choice == "3":
        divisor.smallest_divisor()
    elif choice == "4":
        prime_generator.prime_generator()
    elif choice == "5":
        prime_factorization.prime_factorization()
    elif choice == "6":
        fibonacci.fibonacci_series()
    elif choice == "7":
        power.power_calculator()
    elif choice == "8":
        random_number.random_number_generator()
    elif choice == "9":
        print("Thank you for using Mathematical Problem Solver!")
        break
    else:
        print("Invalid choice. Please try again.")
