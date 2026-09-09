while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Expense Name: ")
        amount = float(input("Amount: "))
        file = open("expenses.txt", "a")
        file.write(name + "'" + str(amount) + "\n")
        file.close()
        print("Exopense Added Successfully!")
    elif choice == '2':
        try:
            file = open("expenses.txt", "r")
            print("\n--- Expenses list ---")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No expenses found:")
    elif choice == '3':
        total = 0
        try:
            file = open("expenses.txt", "r")
            for line in file:
                data = line.strip().split("'")
                total += float(data[1])
            file.close()
            print("Total Expense:", total)
        except FileNotFoundError:
            print("No expenses found!")
    elif choice == "4":
        print("Program Closed!")
        break
    else:
        print("Invalid Choice!")



