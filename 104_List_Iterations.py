# Define a list with 10 names!

# use a for loop to print out all the names in the following format:

# 1 - Welcome Angelo
# 2 - Welcome Monical
# (....)

Eng3637 = ["Daniel", "Shav", "Ally", "Matthew", "Pratheep", "Naila", "Payal", "Hamza", "Omid", "Mujee"]
counter = 1
for classmates in Eng3637:
    print(counter,'-', "Welcome" + " " + classmates)
    counter += 1

import time
# Sweet! Now do the same using a While loop
Eng3637 = ["Daniel", "Shav", "Ally", "Matthew", "Pratheep", "Naila", "Payal", "Hamza", "Omid", "Mujee"]
while counter < 20:
    for classmates in Eng3637:
        print(counter,'-', "Welcome" + " " + classmates)
    counter += 1
    time.sleep(1.6)