# Nice! we're coming to the cool parts!
# here is a dicitonary

my_xmas_present = {
    'Item': 'Millennium Falcon',
    'Price': '13 Billion Dollar',
    'Rating': '5'
}

# Use a for loop to print out the 3 keys
for presents in my_xmas_present:
    print(presents)

for presents in my_xmas_present:
    print(presents, my_xmas_present[presents] )


# Use a for loop to print out the values using the KEYS!
    #hint hint!! my_xmas_present[key]
for presents in my_xmas_present.values():
    print(presents)

# Print both the key and the value in a nice way
for key, value in my_xmas_present.items():
    print(key, ":", value)