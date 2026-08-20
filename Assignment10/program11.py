# Print numbers divisible by m and n.
lst = [10, 12, 15, 18, 20, 24, 30]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Numbers divisible by both:")

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i)
