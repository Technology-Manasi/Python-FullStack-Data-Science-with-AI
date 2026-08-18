#Check Prime Number Using Recursion
def check_prime(n, divisor=2):
    if n < 2:
        return False

    if divisor * divisor > n:
        return True

    if n % divisor == 0:
        return False

    return check_prime(n, divisor + 1)


num = int(input("Enter a number: "))

if check_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")
