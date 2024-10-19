
def detect_character_type(char):
    if char.isalpha():
        return "You entered an alphabet."
    elif char.isdigit():
        return "You entered a number."
    else:
        return "You entered a special character."

user_number = input("Enter a single character: ")

if len(user_number) == 1:
    result = detect_character_type(user_number)
    print(result)
else:
    print("Please enter only one character.")
