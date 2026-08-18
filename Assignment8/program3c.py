#Sum of Series: 1¹ + 2² + 3³ + ... + nⁿ
def power_series_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i ** i)

    return total


n = int(input("Enter n: "))

result = power_series_sum(n)

print("Sum =", result)
