#Armstrong Number Using Recursion
def armstrong_sum(n, digits):
    if n == 0:
        return 0

    digit = n % 10

    return (digit ** digits) + armstrong_sum(n // 10, digits)


def is_armstrong(n):
    digits = len(str(n))

    total = armstrong_sum(n, digits)

    return total == n


num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
