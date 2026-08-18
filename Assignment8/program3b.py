#Sum of Series: 1! + 2! + 3! + ... + n!
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def factorial_series_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


n = int(input("Enter n: "))

result = factorial_series_sum(n)

print("Sum of factorial series =", result)
