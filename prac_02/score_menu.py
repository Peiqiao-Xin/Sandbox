"""

main:
    score ← get_valid_score()
    while true
        print_menu()
        choice ← input().strip().upper()
        if choice = "G"
            score ← get_valid_score()
        else if choice = "P"
            print_result(score)
        else if choice = "S"
            show_stars(score)
        else if choice = "Q"
            print "thank you. goodbye!"
            break
        else
            print "invalid option"

print_menu:
    menu_text ← "
(g) get a valid score (0–100)
(p) print result
(s) show stars
(q) quit
"
    print menu_text

get_valid_score:
    while true
        try
            score ← float(input("enter score (0–100): "))
            if 0 ≤ score ≤ 100
                return score
            else
                print "score must be between 0 and 100."
        catch
            print "invalid input; please enter a number."

determine_status(score):
    if score < 0 or score > 100
        return "invalid score"
    else if score ≥ 90
        return "excellent"
    else if score ≥ 50
        return "passable"
    else
        return "bad"

print_result(score):
    status ← determine_status(score)
    if score.is_integer()
        display_score ← string(int(score))
    else
        display_score ← format(score, ".1f")
    print display_score + " is " + status

show_stars(score):
    stars_count ← int(score)
    print "*" * stars_count

call main
"""

def main():
    """Main menu loop for score operations."""
    score = get_valid_score()
    while True:
        print_menu()
        choice = input(">>> ").strip().upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option")

def print_menu():
    """Display the menu options."""
    menu_text = """
(G) Get a valid score (0–100)
(P) Print result
(S) Show stars
(Q) Quit
"""
    print(menu_text)

def get_valid_score():
    """
    Prompt the user until a valid score (0–100 inclusive) is entered.
    Returns the score as a float.
    """
    while True:
        try:
            score = float(input("Enter score (0–100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input; please enter a number.")

def determine_status(score):
    """
    Determine the status of a given score.
    Returns one of: "Invalid score", "Excellent", "Passable", "Bad".
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_result(score):
    """Print the score and its status."""
    status = determine_status(score)
    # Display score without decimals if it's an integer, otherwise one decimal place
    if score.is_integer():
        display_score = f"{int(score)}"
    else:
        display_score = f"{score:.1f}"
    print(f"{display_score} is {status}")

def show_stars(score):
    """
    Print as many asterisks as the integer part of the score.
    If score is not an integer, cast to int (floor).
    """
    stars_count = int(score)
    print("*" * stars_count)

if __name__ == "__main__":
    main()