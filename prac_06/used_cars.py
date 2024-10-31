"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Yaris", 180)
    my_car.drive(30)
    limo = Car("Hummer", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(f"{limo.name} has fuel: {limo.fuel}")
    print(f"{my_car}")
    print(f"{limo}")


main()
