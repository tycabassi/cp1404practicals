import random


def main():
    fahrenheit = get_temperature_fahrenheit()
    # Returns none first function works fine, troubleshoot after work
    calculate_temperature_celsius(fahrenheit)



def get_temperature_fahrenheit():
    in_file = open('temps_input.txt', 'w')
    for i in range(20):
        random_temperature = random.uniform(-200, 200)
        in_file.write(f"{random_temperature} degrees fahrenheit\n")
    in_file.close()


def calculate_temperature_celsius(fahrenheit):
    in_file = open('temps_input.txt', 'r')
    out_file = open('temps_output.txt', 'w')
    celsius = (fahrenheit - 32) * 5 / 9
    in_file.write(f"{fahrenheit}degrees fahrenheit = {celsius}\n")
    in_file.close()
    out_file.close()


main()
