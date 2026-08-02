start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    temp = num
    count = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** count
        temp = temp // 10

    if sum == num:
        print(num)
