from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

INITIAL_MESSAGE = "Lets drive"
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print(INITIAL_MESSAGE)
    print(MENU)
    choice = input(">>>")
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid choice")
        print(INITIAL_MESSAGE)
        print(MENU)
        choice = input(">>>")


main()
