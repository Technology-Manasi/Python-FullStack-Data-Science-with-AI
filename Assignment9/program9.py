#Calculate m to the Power n Using Recursion
def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)


m = int(input("Enter base (m): "))
n = int(input("Enter power (n): "))

result = power(m, n)

print("Result =", result)
