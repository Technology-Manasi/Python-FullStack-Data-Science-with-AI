n = int(input("Enter a number: "))

temp = n
count = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
