MENU = """(C)elsius ---> Fahrenheit
(F)ahrenheit ---> Celsius"""


def main():
    print(MENU)
    choice = input(">>>").upper()
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} F")
    else:
        print("Invalid choice")


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


main()
