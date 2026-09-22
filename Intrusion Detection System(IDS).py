from datetime import datetime
real_username = "Rehan"
real_password = "Cyber123"
attempts = 0
print("=====  Intrusion Detection System =====")
while attempts < 3:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == real_username and password == real_password:
        print("\nLogoin Successful!")
        file = open("security_log.txt", "a")
        file.write("Time : " + str(datetime.now()) + "\n")
        file.write("Username : " + username + "\n")
        file.write("Status : SUCCESS\n")
        file.close()
        break
    else:
        attempts += 1
        print("\nInvalid Username or Password")
        print("Attempts Left:", 3 - attempts)
        file = open("security_log.txt", "a")
        file.write("\n--------------------------------\n")
        file.write("Time : " + str(datetime.now()) + "\n")
        file.write("Username : " + username + "\n")
        file.write("Status : FAILED\n")
        file.close()
        if attempts == 3:
            print("\nALERT! ACCOUNT LOCKED")
            print("Suspicious Activity Detected!")
            file = open("security_log.txt", "a")
            file.write("ALERT! ACCOUNT LOCKED\n")
            file.close()


