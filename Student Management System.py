students = {}
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. update Student")
    print("6.  Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students[name] = marks
        print("Student added successfully!")
    elif choice == '2':
        if students:
            for name, marks in students.items():
                print(name, ":", marks)
        else:
            print("No students found.")
    elif choice == '3':
        name = input("Enter student name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found.")
    elif choice == '4':
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    elif choice == '5':
        name = input("Enter student name to update: ")
        if name in students:
            marks = input("Enter new marks: ")
            students[name] = marks
            print("Student updated successfully!")
        else:
            print("Student not found.")
    elif choice == '6':
        print("Program Closing...")
        break
