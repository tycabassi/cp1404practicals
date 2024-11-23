from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represents the High-rollers Silver Service Taxi"""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialises the Silver Service Taxi class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km += fanciness

    def __str__(self):
        """Returns a string representation of the Silver Service Taxi"""
        return f"{super().__str__()} + $ {self.flag_fall:.2f} flag fall"
