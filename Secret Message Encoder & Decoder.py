while True:
    print("\n===== Secret Message Encoder & Decoder =====")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Count Characters")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        text = input("Enter Message: ")
        result = ""
        for ch in text:
            result += chr(ord(ch) + 3)
        print("Encoded Message:", result)
    elif choice == "2":
        text = input("Enter Encoded Message: ")
        result = ""
        for ch in text:
            result += chr(ord(ch) - 3)
        print("Decoded Message:", result)
    elif choice == "3":
        text = input("Enter Message: ")
        print("Total Characters:", len(text))
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
