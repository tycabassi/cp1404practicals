import random


def main():
    create_input_file(15)
    in_file = open('temps_input.txt', 'r')
    out_file = open('temps_output.txt', 'w')
    for line in in_file:
        result = convert_fahrenheit_to_celsius(float(line))
        print(result, file=out_file)
    in_file.close()
    out_file.close()


def create_input_file(quantity):
    """Write number (quantity) of temperatures to file."""
    temperatures_file = open("temps_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temperatures_file)
    temperatures_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


main()
