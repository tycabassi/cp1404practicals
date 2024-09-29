
import random
YEARS = 10
MENU = "Welcome to the starting Gopher Population Simulator"
def main():
    for i in range(YEARS):
        while i < YEARS:
            population = int(input("Starting Population: "))
            calculate_population(population)
            i += 1
            print(f"Year: {i}")
            print(f"Population: {population}")



def calculate_population(population):
    born_rate = random.randint(10,20)
    death_rate = random.randint(5, 25)
    print(f"Born rate: {born_rate}")
    print(f"Deathrate: {death_rate}")





# def gopher_deaths_calculator(starting_population):






main()