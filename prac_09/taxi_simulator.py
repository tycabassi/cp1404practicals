from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

INITIAL_MESSAGE = "Lets drive"
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print(INITIAL_MESSAGE)
    print(MENU)
    current_taxi = None
    choice = input(">>>")
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            print(Taxi("Prius",100))
            print(SilverServiceTaxi("Limo", 100,2))
            print(SilverServiceTaxi("Hummer",200,4))
            pass
            current_taxi = True
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            pass
        else:
            print("Invalid choice")
        print(INITIAL_MESSAGE)
        print(MENU)
        choice = input(">>>")


main()
