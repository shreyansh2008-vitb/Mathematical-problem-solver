def prime_factorization():
    n = int(input("Enter a number: "))

    if n <= 1:
        print("Prime factorization is not defined for this number.")
        return

    print("Prime factors:", end=" ")

    divisor = 2

    while n > 1:
        while n % divisor == 0:
            print(divisor, end=" ")
            n = n // divisor

        divisor += 1

    print()

prime_factorization()
