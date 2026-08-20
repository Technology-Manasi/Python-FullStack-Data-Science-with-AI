# Create a duplicate of an existing list
lst = [5, 10, 15, 20]
duplicate = []

for i in lst:
    duplicate = duplicate + [i]

print("Original:", lst)
print("Duplicate:", duplicate)
