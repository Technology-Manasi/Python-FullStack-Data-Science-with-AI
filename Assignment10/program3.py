#Find the second largest element.
lst = [12, 55, 78, 23, 90, 67]

first = lst[0]
second = -999999

for i in lst:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second Largest =", second)
