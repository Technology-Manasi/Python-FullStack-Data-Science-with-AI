students = int(input("Enter number of students: "))

total_percentage = 0

for i in range(students):
    print("Student", i + 1)

    total = 0

    for j in range(5):
        marks = int(input("Enter marks: "))
        total = total + marks

    percentage = total / 5

    print("Percentage =", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / students

print("Average Percentage =", average)
