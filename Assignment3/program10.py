gender = input("Enter Gender (male/female): ")
age = int(input("Enter Age: "))

if gender == "male":
    if age >= 21:
        print("Eligible")
    else:
        print("Not Eligible")

elif gender == "female":
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
