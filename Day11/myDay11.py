# Day 11
# 🔐Password Strength Checker in Python

def check_password(password):
    upper_chars, lower_chars, special_chars, digits, length = 0, 0, 0, 0, len(password)
    
    if length < 6:
        print("Password must be at least 6 characters long!\n")
    else:
        for char in password:
            if char.isupper():
                upper_chars += 1
            elif char.islower():
                lower_chars += 1
            elif char.isdigit():
                digits += 1
            else:
                special_chars += 1
    
    if upper_chars and lower_chars and digits and special_chars:
        if length >= 10:
            print("The strength of the password is strong.")
        else:
            print("The strength of the password is medium.")
    else:
        if not upper_chars:
            print("Password must contain at least one uppercase character!\n")
        elif not lower_chars:
            print("Password must contain at least one lowercase character!\n")
        elif not special_chars:
            print("Password must contain at least one special character!\n")
        else:
            print("Password must contain at least one digit!\n")
            
password = input("Please enter a password: ")
check_password(password)
