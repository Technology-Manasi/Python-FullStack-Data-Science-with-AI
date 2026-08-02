userid = "admin"
password = "1234"

for i in range(3):
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")

    if uid == userid and pwd == password:
        print("Login Successful")
        break
    else:
        print("Wrong User ID or Password")

else:
    print("Program Terminated")
