import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1
    else:
        score -= 2

    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2

    weak_passwords = ["123456", "password", "admin", "qwerty"]
    if password.lower() in weak_passwords:
        score -= 3

    if score <= 3:
        return "Weak Password"
    elif score <= 6:
        return "Medium Password"
    else:
        return "Strong Password"

pwd = input("Enter password: ")
print("Result:", check_password_strength(pwd))