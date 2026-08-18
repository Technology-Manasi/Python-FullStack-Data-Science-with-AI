#Check Palindrome Number
def check_palindrome(n):
    reverse = reverse_number(n)

    if n == reverse:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if check_palindrome(n):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
