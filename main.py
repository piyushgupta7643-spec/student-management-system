students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    student = {
        "name": name,
        "roll": roll
    }

    students.append(student)
    print("Student added successfully!")

def show_students():
    for student in students:
        print(student["name"], student["roll"])

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
