from prac_07.guitar import Guitar


def main():
    guitars = []
    get_guitar_details(guitars)
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = input("Year: ")
        cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, year, cost)
        print(f"{new_guitar} added")
        guitar_name = input("Name: ")
        guitars.append(new_guitar)
    sort_guitars(guitars)


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
