LOWER_CASE_REQUIRED = True
UPPER_CASE_REQUIRED = True
NUMBERS_REQUIRED = True
SPECIAL_CHARACTERS_REQUIRED = False
REQUIREMENTS = [LOWER_CASE_REQUIRED, UPPER_CASE_REQUIRED, NUMBERS_REQUIRED, SPECIAL_CHARACTERS_REQUIRED]
MIN_CHARACTERS = 5
MAX_CHARACTERS = 15
SPECIAL_CHARACTERS = "!@#$%^&()_-`~,./'[]<>?{}|\\"


def main():
    print("""Please enter a valid password
your password must be between {} and {} characters long and contain:""".format(MIN_CHARACTERS, MAX_CHARACTERS))
    if LOWER_CASE_REQUIRED is True:
        print("Must contain 1 or more lower case letters")
    if UPPER_CASE_REQUIRED is True:
        print("Must contain 1 or more upper case letters")
    if NUMBERS_REQUIRED is True:
        print("Must contain 1 or more numbers")
    if SPECIAL_CHARACTERS_REQUIRED is True:
        print("Must contain 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    is_valid_password(password)
    valid_password, character_count = is_valid_password(password)
    while not valid_password:
        print("Not a valid password!")
        password = input("> ")
        is_valid_password(password)
        valid_password, character_count = is_valid_password(password)
    print("Valid password!")
    print("Your {} letter password is {}".format(len(password), password))


def is_valid_password(password):
    lower_case_count = 0
    upper_case_count = 0
    numbers_case_count = 0
    special_characters_count = 0
    character_count = 0
    checked_count = 0
    true_counters = 0
    for character in password:
        character_count += 1
        if character.islower():
            lower_case_count += 1
        elif character.isupper():
            upper_case_count += 1
        elif character.isnumeric():
            numbers_case_count += 1
        elif character in SPECIAL_CHARACTERS:
            special_characters_count += 1
    counter_checker = [lower_case_count, upper_case_count, numbers_case_count, special_characters_count]
    if character_count > MIN_CHARACTERS and character_count < MAX_CHARACTERS:
        for i in REQUIREMENTS:
            if i is True:
                true_counters += 1
                print("i is ", i)
                if counter_checker[i] != 0:
                    checked_count += 1
        if checked_count == true_counters:
            return True, character_count
        else:
            return False, character_count
    else:
        return False, character_count


main()
