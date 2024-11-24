class Band:
    """Create a band class"""

    def __init__(self, name):
        """Initialise the band class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({", ".join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Displays what instrument the artist plays."""
        for musician in self.musicians:
            print(musician.play())
