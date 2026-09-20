while True:
    print("\n===== File Encryption Tool =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. View Encrypted File")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        file = open("secret.txt", "r")
        text = file.read()
        file.close()
        encrypted = ""
        for ch in text:
            encrypted += chr(ord(ch) + 3)
        file = open("encrypted.txt", "w")
        file.write(encrypted)
        file.close()
        print("File Encrypted Successfully.")
    elif choice == "2":
        file = open("encrypted.txt", "r")
        text = file.read()
        file.close()
        decrypted = ""
        for ch in text:
            decrypted += chr(ord(ch) - 3)
        file  = open("decrypted.txt", "w")
        file.write(decrypted)
        file.close()
        print("File Decrypted Successfully.")
    elif choice == "3":
        file = open("encrypted.txt", "r")
        text = file.read()
        file.close()
        print("Encrypted File Content:\n", text)
    elif choice == "4":
        print("Program Closed!")
        break
    else:
        print("Invalid Choice!")



