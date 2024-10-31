# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.40
# print(f"My guitar: {name}, first made in {year}")


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"


guitar_details = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar_details)
