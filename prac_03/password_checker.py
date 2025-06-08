"""

main
  print "please enter a valid password"
  print rules (min_length to max_length, upper, lower, digit, [special])
  pwd ← input("> ")
  while not valid(pwd)
    print "invalid password!"
    pwd ← input("> ")
  print "your", len(pwd), "character password is valid:", pwd

valid(pwd)
  if len(pwd) < MIN_LENGTH or len(pwd) > MAX_LENGTH
    return false
  lower←0; upper←0; digit←0; special←0
  for c in pwd
    if c.isdigit()   then digit←digit+1
    elif c.islower() then lower←lower+1
    elif c.isupper() then upper←upper+1
    elif c in SPECIAL_CHARACTERS then special←special+1
  if lower==0 or upper==0 or digit==0
    return false
  if IS_SPECIAL_CHARACTER_REQUIRED and special==0
    return false
  return true
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1
        # Notice the appropriate use of if, elif, no else pattern
    # TODO: if any of the 'normal' counts are zero, return False
    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()