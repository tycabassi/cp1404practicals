from prac_07.guitar import Guitar


def main():
    guitars = []
    get_guitar_details(guitars)
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))  # Needs to be and int as its subtracted from CURRENT_YEAR in is_vintage()
        cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, year, cost)
        print(f"{new_guitar} added")
        guitar_name = input("Name: ")


def get_guitar_details(guitars):
    with open("guitars.csv") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


def sort_guitars(guitars):
    guitars.sort()  # Sorts using __lt__ method used in guitar.py
    for guitar in guitars:
        print(guitar)


main()
