from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name,fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability
