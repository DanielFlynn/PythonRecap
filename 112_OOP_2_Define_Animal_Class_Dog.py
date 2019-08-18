# Needs to inherit from animal

# Need to have two of it's own methods
# it needs polymorph the make a noise method

from OOP_2_Define_Animal_Class import *

class Dog(Animal):
    def __init__(self, name, alive, colour, breed):
        super().__init__(name, alive)
        self.colour = colour
        self.breed = breed

    def teeth(self):
        return "Bite"

    def tail(self):
        return "Wag"

    def noise(self):
        return "Bark"
