#Create a new list containing cubes
lst = [1, 2, 3, 4]
cube = []

for i in lst:
    cube = cube + [i * i * i]

print("Cube List:", cube)
