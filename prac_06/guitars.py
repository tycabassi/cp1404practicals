from prac_06.guitar import Guitar

my_guitars = []
print("My Guitars!")
guitar_name = input("Name: ")
while guitar_name != "":
    year = int(input("Year: ")) # Needs to be and int as its subtracted from CURRENT_YEAR in is_vintage()
    cost = float(input("Cost: $"))
    new_guitar = Guitar(guitar_name, year, cost)
    print(f"{new_guitar} added")
    my_guitars.append(new_guitar)
    guitar_name = input("Name: ")

for i, guitar in enumerate(my_guitars):
    vintage_string = ""
    if guitar.is_vintage() is True:
        vintage_string = "(vintage)"
    print(f"Guitar {i+1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
