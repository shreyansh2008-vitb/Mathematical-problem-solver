from square_root import square_root
from gcd import gcd_calculator
from divisor import smallest_divisor
from prime_generator import prime_generator


def main():
    while True:
        print("\n===== Python Mathematical Problem Solver =====")
        print("1. Square Root Calculator")
        print("2. GCD Calculator")
        print("3. Smallest Divisor Finder")
        print("4. Prime Number Generator")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            square_root()

        elif choice == "2":
            gcd_calculator()

        elif choice == "3":
            smallest_divisor()

        elif choice == "4":
            prime_generator()

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
