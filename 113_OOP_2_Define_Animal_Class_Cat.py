# Needs to inherit from animal


# Need to have two of it's own methods
# it needs polymorph the make a noise method

from OOP_2_Define_Animal_Class import *

class Cat(Animal):
    def __init__(self, name, alive, colour):
        super().__init__(name, alive)
        self.colour = colour

    def noise(self):
        return "Meoow"

    def claws(self):
        return "Scratch"

    def teeth(self):
        return "Hiss"
