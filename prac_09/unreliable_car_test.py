from prac_09.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Reliable Car", 200, 99)
    unreliable_car = UnreliableCar("Unreliable Car", 100, 11)

    for i in range(1,10):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


main()
