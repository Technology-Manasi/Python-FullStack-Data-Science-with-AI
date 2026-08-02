n = int(input("Enter number of prime numbers: "))

count_prime = 0
num = 2

while count_prime < n:

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)
        count_prime = count_prime + 1

    num = num + 1
