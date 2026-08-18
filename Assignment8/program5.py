#Sum of All Prime Numbers Between 1 to n.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def sum_prime_numbers(n):
    total = 0

    for i in range(1, n + 1):
        if is_prime(i):
            total = total + i

    return total


n = int(input("Enter n: "))

result = sum_prime_numbers(n)

print("Sum of prime numbers =", result)
