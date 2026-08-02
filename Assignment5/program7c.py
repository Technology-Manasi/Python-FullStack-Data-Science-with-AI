n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    sum = sum + 2 ** i

print("Sum =", sum)
