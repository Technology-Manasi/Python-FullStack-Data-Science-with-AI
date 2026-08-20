# Reverse the list
lst = [1, 2, 3, 4, 5]
rev = []

i = len(lst) - 1

while i >= 0:
    rev = rev + [lst[i]]
    i = i - 1

print("Reversed List:", rev)
