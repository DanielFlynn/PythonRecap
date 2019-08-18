# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????

cars = ["Audi", "BMW", "Vauxhall", "Skoda", "Toyota"]
# Print the lists and check it's type
print (cars)
print(type(cars))

# Print the list's first object
print(cars[0])

# Print the list's second object
print(cars[1])

# Print the list's last object
print(cars[4])

# Re-define the first item on the list and
cars[0] = "Suzuki"
print(cars)

# Re-define another item on the list and print all the list
cars[3] = "Honda"
print(cars)

# Add an item to the list and print the list
cars.append("Aston Martin")
print(cars)
# Remove an item from the list and print the list
cars.remove("Honda")
print(cars)
# Add two items to list and print the list
cars.append("Fiat")
cars.append("Ferrari")
print(cars)