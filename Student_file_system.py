while True:
    print("\n===== Student File system =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter student name: ")
        marks = input("Enter Marks: ")
        file = open("students.txt", "a")
        file.write(name + "," + marks + "\n")
        file.close()
        print("Student Saved!")
    elif choice == '2':
        try:
            file= open("students.txt" , "r")
            for line in file:
               print(line.strip())
            file.close()
        except FileNotFoundError:
            print("No data found!")
    elif choice == '3':
        search_name = input("Enter student name to search: ")
        try:
            file = open("students.txt", "r")
            found = False
            for line in file:
                if search_name in line:
                    print(line.strip())
                    found = True
            if not found:
                print("Student not found!")
            file.close()
        except FileNotFoundError:
            print("No data found!")
    elif choice == '4':
        delete_name = input("Enter student name to delete: ")
        try:
            file = open("students.txt", "r")
            lines = file.readlines()
            file.close()
            file = open("students.txt", "w")
            found = False
            for line in lines:
                if delete_name not in line:
                    file.write(line)
                else:
                    found = True
            file.close()
            if found:
                print("Student deleted!")
            else:
                print("Student not found!")
        except FileNotFoundError:
            print("No data found!")
    elif choice == '5':
        print("Program Closing...")
        break
    else:
        print("Invalid choice! Please try again.")
    
             