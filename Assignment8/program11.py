#Check Armstrong Number.
def check_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + (digit ** digits)
        n = n // 10

    if total == original:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if check_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
