
# DOES NOT inherit from anywhere

# need to have:
# date
# reason visit
# a place to  hold an animal


# need to have the method:
    # add an animal.

class Vet_Visit():
    def __init__(self, date, reason_visit, storage):
        self.date = date
        self.reason_visit = reason_visit
        self.storage = storage

    def Vetinarian (self):
        return 'Antibiotics'


class Animal():