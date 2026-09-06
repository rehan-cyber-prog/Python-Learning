while True:
    print("\n===== Login System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        file = open("users.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()
        print("Registration Successfully!")
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        found = False
        try:
            file = open("users.txt", "r")
            for line in file:
                data = line.strip().split(",")
                if data[0] == username and data[1] == password:
                    found = True
                    break
            file.close()
            if found:
                print("Login Successfullly!")
            else:
                print("Invalid Username or Password!")
        except FileNotFoundError:
            print("No users found!")
    elif choice == '3':
        print("Program Closing...")
        break
            