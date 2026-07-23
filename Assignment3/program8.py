import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)

    print("Captcha =", captcha)

    user = int(input("Enter Captcha: "))

    if user == captcha:
        print("Login Successful")
    else:
        print("Wrong Captcha")
else:
    print("Invalid User ID or Password")
