from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

INITIAL_MESSAGE = "Lets drive"
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    print(INITIAL_MESSAGE)
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0
    choice = input(">>>")
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            current_taxi = get_taxi_choice(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far?"))
                current_taxi.start_fare()
                print(f"The {current_taxi} trip cost you{current_taxi.get_fare(distance)} miles")

        else:
            print("Invalid choice")
        print(INITIAL_MESSAGE)
        print(MENU)
        choice = input(">>>")


def display_taxis(taxis):
    print("Taxis available")
    for i, car in enumerate(taxis):
        print(f"{i} - {car}")


def get_taxi_choice(taxis):
    choice_of_taxi = int(input("Choose Taxi: "))
    current_taxi = taxis[choice_of_taxi]
    return current_taxi


main()
