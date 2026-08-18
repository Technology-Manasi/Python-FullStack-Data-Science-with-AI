#Sum of Series: 1! + 2! + 3! + ... + n!
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_factorial(n):
    if n == 0:
        return 0
    else:
        return factorial(n) + sum_factorial(n - 1)


n = int(input("Enter n: "))

result = sum_factorial(n)

print("Sum of factorial series =", result)
