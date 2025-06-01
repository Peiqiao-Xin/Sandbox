"""

main:
    score ← float(input("enter score: "))
    display determine_status(score)

determine_status(score):
    if score < 0 or score > 100
        return "invalid score"
    else if score ≥ 90
        return "excellent"
    else if score ≥ 50
        return "passable"
    else
        return "bad"

call main
"""



def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()