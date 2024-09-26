MENU = """(G)et a valid score(must be 0-100 inclusive)
(P)rint result
(S)how stars (This should print as many stars as the score)
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            determine_score(score)
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>: ").upper()


def get_valid_score():
    score = int(input("Enter a score between 1 and 100: "))
    while score < 1 or score > 100:
        print("Invalid")
        score = int(input("Enter a score between 1 and 100: "))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()