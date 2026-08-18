#Sum of All Odd Numbers Between 1 to n.
def sum_odd_numbers(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total = total + i

    return total


n = int(input("Enter n: "))

result = sum_odd_numbers(n)

print("Sum of odd numbers =", result)
