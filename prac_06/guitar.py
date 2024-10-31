# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.40
# print(f"My guitar: {name}, first made in {year}")

CURRENT_YEAR = 2024


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        return CURRENT_YEAR - self.year


guitar_details = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar_details)
print(guitar_details.get_age())
