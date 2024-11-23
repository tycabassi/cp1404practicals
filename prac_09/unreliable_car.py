import random
from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_generation = random.randint(1, 100)
        if reliability_generation >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
