"""

constant minimum_length = 4

main:
    password ← get_password(minimum_length)
    print_asterisks(password)

get_password(min_length):
    display "enter password of at least [min_length] characters: "
    password ← input
    while length(password) < min_length
        display "password too short"
        display "enter password of at least [min_length] characters: "
        password ← input
    return password

print_asterisks(seq):
    display "*" * length(seq)

call main
"""

MINIMUM_LENGTH = 4


def version_1():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")

    print('*' * len(password))


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()