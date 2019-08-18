# Needs to inherit from animal


# Need to have two of it's own methods
# it needs polymorph the make a noise method

from Class_Animal import *


class Duck(Animal):
    def __init__(self, name, alive, beak):
        super().__init__(name, alive)
        self.beak = beak

    def wings(self):
        return "Flap"

    def webbed_feet(self):
        return "Scurry"

    def sound(self):
        return "QUACK!"

