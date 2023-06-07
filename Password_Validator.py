def Password_Validator(password):
    valid = True
    if len(password) < 6 or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
        valid = False

    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        valid = False
    counter_of_digits = 0
    for char in password:
        if char.isdigit():
            counter_of_digits +=1
    if counter_of_digits < 2:
        print(f"Password must have at least 2 digits")
        valid = False
    return valid


some_password = input()
is_valid = Password_Validator(some_password)
if is_valid:
    print("Password is valid")
