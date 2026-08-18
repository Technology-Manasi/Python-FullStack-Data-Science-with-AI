#Fibonacci Series Using Function.
def fibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c


n = int(input("Enter number of terms: "))

print("Fibonacci Series:")

fibonacci(n)
