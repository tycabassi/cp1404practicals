from prac_07.guitar import Guitar


def main():
    in_file = open("guitars.csv")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], parts[1], parts[2])
        print(guitar)


main()
