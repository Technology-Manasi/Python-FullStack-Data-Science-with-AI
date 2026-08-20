# Print list after removing even numbers.

lst = [1, 2, 3, 4, 5, 6, 7, 8]

odd = []

for i in lst:
    if i % 2 != 0:
        odd = odd + [i]

print("List after removing even numbers:", odd)
