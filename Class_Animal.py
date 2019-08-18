#Define a class Animal

# it should:
    # have properties:
    # alive
    # name

# it should be able to:

# eat
# sleep
# inhale
# exhale
# make sound: HI!

class Animal():
    def __init__(self, name, alive):
        self.name = name
        self.alive = alive

    def eat(self):
        return "Nom Nom"

    def sleep(self):
        return "zzzzzzz"

    def inhale(self):
        return "gasp"

    def exhale(self):
        return "hhhhhhhhhhh"

    def sound(self):
        return "HI!"