"""

main:
    display menu_text
    choice ← input().upper()
    while choice ≠ "Q"
        if choice = "C"
            c ← float(input("celsius: "))
            f ← c * 9 / 5 + 32
            display "result: [f formatted to 2 decimals] f"
        else if choice = "F"
            f ← float(input("fahrenheit: "))
            c ← (f - 32) * 5 / 9
            display "result: [c formatted to 2 decimals] c"
        else
            display "invalid option"
        display menu_text
        choice ← input().upper()
    display "thank you"

call main
"""


MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    """Temperature conversion program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()