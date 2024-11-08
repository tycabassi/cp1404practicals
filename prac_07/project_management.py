"""Estimated time: 1hr 45
Actual time: """
import datetime

MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project"
        "(U)pdat project\n(Q)uit")


def main():
    print(MENU)
    choice = input("Enter a choice: ").lower()
    while choice != "q":
        if choice == "l":
            pass
        elif choice == "s":
            pass
        elif choice == "d":
            pass
        elif choice == "f":
            pass
        elif choice == "a":
            pass
        elif choice == "u":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter a choice: ").lower()


# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))


main()
