def smallest_divisor():
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Smallest divisor is not defined for this number.")
        return

    for i in range(2, n + 1):
        if n % i == 0:
            print("Smallest divisor =", i)
            break

smallest_divisor()
