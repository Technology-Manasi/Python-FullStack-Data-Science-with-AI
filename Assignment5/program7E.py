x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
denominator = 1

for i in range(1, n + 1):

    term = sign * (x ** i) / denominator

    sum = sum + term

    sign = sign * -1
    denominator = denominator + 2

print("Sum =", sum)
