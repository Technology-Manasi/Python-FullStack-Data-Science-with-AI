#Alphabet Triangle
rows = 5

for i in range(1, rows + 1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
