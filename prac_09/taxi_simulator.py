from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

INITIAL_MESSAGE = "Lets drive"
MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate a taxi service"""
    print(INITIAL_MESSAGE)
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fee = 0
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
                current_taxi.drive(distance)
                print(f"The {current_taxi} trip cost you ${current_taxi.get_fare()}")
                total_fee += current_taxi.get_fare()
                print(f"Bill to date: ${total_fee}")
        else:
            print("Invalid choice")
        print(INITIAL_MESSAGE)
        print(MENU)
        choice = input(">>>")
    print(f"Total bill: ${total_fee}")


def display_taxis(taxis):
    """Displays all the taxis"""
    print("Taxis available")
    for i, car in enumerate(taxis):
        print(f"{i} - {car}")


def get_taxi_choice(taxis):
    """Gets a taxi choice from the user and returns it"""
    choice_of_taxi = int(input("Choose Taxi: "))
    current_taxi = taxis[choice_of_taxi]
    return current_taxi


main()
