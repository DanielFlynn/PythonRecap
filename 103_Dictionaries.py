# Dictionaries!

# Fine a dictionary with cool things inside!
    # Examples: Christmas list with item and price
    # complete the sentence:
    # Dictionaries are organise using: keys and values
vehicle = {
    "type": "Car",
    "brand": "Vauxhall",
    "colour": "Black"
}

# Print the dictionary and check it's type
print(vehicle)
print(type(vehicle))

# Print the dictionary keys
print(vehicle.keys())

# Print the dictionary's values
print(vehicle.values())

# Print the dictionary first key and value together


# Re-define the value on the dictionary using it's key
vehicle ["type"] = "Motorcycle"
print(vehicle)
# Re-define another value on the dictionary using it's key
vehicle ["brand"] = "Toyota"
print(vehicle)

# Add an a new key  - value to the dictionary (say rating)
vehicle ["engine"] = 1.4
print(vehicle)

# Access only the value of the last key you created from the dictionary
print (vehicle ["engine"])

# Re-define that value in the dictionary
vehicle ["engine"] = 1.8
print(vehicle["engine"])