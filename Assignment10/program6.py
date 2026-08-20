#Remove duplicates from the list.
lst = [1, 2, 3, 2, 4, 1, 5]
new = []

for i in lst:
    found = False

    for j in new:
        if i == j:
            found = True

    if found == False:
        new = new + [i]

print("List without duplicates:", new)
