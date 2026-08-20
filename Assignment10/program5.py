# Check if an element is present and count occurrences.
lst = [10, 20, 30, 20, 40, 20]

num = int(input("Enter number: "))

count = 0

for i in lst:
    if i == num:
        count = count + 1

if count > 0:
    print("Element Present")
    print("Occurrences =", count)
else:
    print("Element Not Present")
