"""Estimated time: 35-40 minutes
Time taken: 46 minutes"""

CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Stores guitar information"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize the guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of the guitar properties"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether the guitar is vintage"""
        if CURRENT_YEAR - self.year > VINTAGE_AGE:
            return True
        return False
