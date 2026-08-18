#Sum of Series: 1 + 2 + 3 + ... + n
def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total


n = int(input("Enter n: "))

result = sum_series(n)

print("Sum =", result)
