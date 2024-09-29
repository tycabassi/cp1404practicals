import random

YEARS = 10
MENU = "Welcome to the starting Gopher Population Simulator"


def main():
    print(MENU)
    population = int(input("Starting Population: "))
    for i in range(YEARS):
        gophers_born, gopher_deaths = calculate_population_fluctuation(population)
        new_population = (population + gophers_born) - gopher_deaths
        i += 1
        print(f"{gophers_born} gophers were born. {gopher_deaths} died.")
        print(f"Population: {new_population}")
        print(f"Year: {i}\n")


def calculate_population_fluctuation(population):
    born_chance = random.randint(10, 20)
    death_chance = random.randint(5, 25)
    gophers_born = (population * born_chance / 100)
    gopher_deaths = (population * death_chance / 100)
    return gophers_born, gopher_deaths





main()
