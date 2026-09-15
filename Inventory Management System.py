while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":
        name = input("Enter Product Name: ")
        quantity = input("Enter Quantity: ")
        price = input("Enter Price: ")

        file = open("inventory.txt", "a")
        file.write(name + "," + quantity + "," + price + "\n")
        file.close()

        print("Product Added Successfully!")

    # View Product
    elif choice == "2":
        try:
            file = open("inventory.txt", "r")

            print("===== Product List =====")

            for line in file:
                print(line.strip())

            file.close()

        except FileNotFoundError:
            print("No Products Found!")

    # Search Product
    elif choice == "3":
        search = input("Enter Product Name: ")
        found = False

        try:
            file = open("inventory.txt", "r")

            for line in file:
                data = line.strip().split(",")

                if search.strip().lower() in data[0].strip().lower():
                    print("Found:", line.strip())
                    found = True

            file.close()

            if not found:
                print("Product Not Found!")

        except FileNotFoundError:
            print("No Products Found!")

    # Update Quantity
    elif choice == "4":
        product = input("Enter Product Name: ")
        new_quantity = input("Enter New Quantity: ")

        try:
            file = open("inventory.txt", "r")
            lines = file.readlines()
            file.close()

            file = open("inventory.txt", "w")
            found = False

            for line in lines:
                data = line.strip().split(",")

                if len(data) >= 3 and data[0].strip().lower() == product.strip().lower():
                    file.write(data[0] + "," + new_quantity + "," + data[2] + "\n")
                    found = True
                else:
                    file.write(line)

            file.close()

            if found:
                print("Quantity Updated!")
            else:
                print("Product Not Found!")

        except FileNotFoundError:
            print("No Products Found!")

    # Delete Product
    elif choice == "5":
        product = input("Enter Product Name: ")

        try:
            file = open("inventory.txt", "r")
            lines = file.readlines()
            file.close()

            file = open("inventory.txt", "w")
            found = False

            for line in lines:
                data = line.strip().split(",")

                if len(data) >= 3 and data[0].strip().lower() != product.strip().lower():
                    file.write(line)
                else:
                    found = True

            file.close()

            if found:
                print("Product Deleted!")
            else:
                print("Product Not Found!")

        except FileNotFoundError:
            print("No Products Found!")

    # Exit
    elif choice == "6":
        print("Program Closed!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice!")