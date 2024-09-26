MENU = """(C)elsius --> Fahrenheit
(F)ahrenheit --> Celsius"""


def main():
    print(MENU)
    choice = input(">>>").upper()
    if choice == "C":
        convert_celsius_to_fahrenheit()
    elif choice == "F":
        convert_fahrenheit_to_celsius()
    else:
        print("Invalid choice")


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")




main()