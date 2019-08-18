# Needs to inherit from animal

# Need to have two of it's own methods
# it needs polymorph the make a noise method

from Class_Animal import *

class Dog(Animal):
    def __init__(self, name, alive, breed):
        super().__init__(name, alive)
        self.breed = breed


    def fetch(self):
        return "Stick"

    def tail(self):
        return "Wag"

    def sound(self):
        return "WOOF!"