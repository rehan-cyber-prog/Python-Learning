print("===== Password Strength Checker =====")
password = input("Enter Password: ")
score = 0
if len(password) >= 8:
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(not c.isalnum() for c in password):
    score += 1
if "123" in password:
    print("Warning: Do not use 123 in password!")
    print("\nSecurity Score:", score, "/5")
if score == 5:
    print("Very Strong Password")
elif score == 3:
    print("Medium Password")
else:
    print("Weak Password")
