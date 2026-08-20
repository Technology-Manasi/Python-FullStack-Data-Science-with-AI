# Remove all occurrences of a given element.

lst = [10, 20, 30, 20, 40, 20]

num = int(input("Enter element to remove: "))

new = []

for i in lst:
    if i != num:
        new = new + [i]

print("Updated List:", new)
