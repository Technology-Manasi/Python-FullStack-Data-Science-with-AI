# Separate even and odd numbers.
n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter number: "))
    lst = lst + [num]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even = even + [i]
    else:
        odd = odd + [i]

print("Even List:", even)
print("Odd List:", odd)
