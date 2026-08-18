#Sum of n Numbers Using Recursion
def sum_n_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_n_numbers(n - 1)


n = int(input("Enter n: "))

result = sum_n_numbers(n)

print("Sum =", result)
