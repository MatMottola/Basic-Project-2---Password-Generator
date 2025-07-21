import random
import string

def generate_password(min_length = 7, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    excluded_chars = ":,.+-><°¬¢£³¨^;?`~²¹+\\/=§]}|ª{[º)('\""
    special = ''.join([c for c in string.punctuation if c not in excluded_chars])

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


while True:
    try:
        min_length = int(input("Enter minimum length of password: "))
        if min_length > 0:
            break
        else:
                print("Please enter a number greater than zero.")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")


while True:
    num_input = input("Should it contain numbers? (yes/no): ").lower()
    if num_input in ['yes', 'no']:
        has_number = num_input =='yes'
        break
    else:
        print("Please enter 'yes' or 'no'.")


while True:
    special_input = input("Should it contain special characters? (yes/no): ").lower()
    if special_input in ['yes', 'no']:
        has_special = special_input =='yes'
        break
    else:
        print("Please enter 'yes' or 'no'.")

    



pwd = generate_password(min_length, has_number, has_special)
print("The Generated Password is:",pwd)


