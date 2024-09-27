import random


def main():
    in_file = open('temps_input.txt', 'w')
    for i in range(20):
        random_temperature = random.uniform(-200, 200)
        in_file.write(f"{random_temperature} degrees fahrenheit\n")
    in_file.close()


main()
