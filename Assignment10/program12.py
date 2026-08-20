# Create three lists: numbers, squares, and cubes.

numbers = [1, 2, 3, 4, 5]

square = []
cube = []

for i in numbers:
    square = square + [i * i]
    cube = cube + [i * i * i]

print("Numbers:", numbers)
print("Squares:", square)
print("Cubes:", cube)
