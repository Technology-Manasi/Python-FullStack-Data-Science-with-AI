#Alphabet Odd Pattern
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    ch = ord('A')
    for j in range(2 * i - 1):
        print(chr(ch), end=" ")
        ch += 1
    print()
