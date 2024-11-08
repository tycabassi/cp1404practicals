from prac_07.guitar import Guitar


def main():
    guitars = []
    get_guitar_details(guitars)
    guitars.sort() # Sorts using __lt__ method used in guitar.py
    for guitar in guitars:
        print(guitar)


def get_guitar_details(guitars):
    with open("guitars.csv") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
    return guitars


main()
