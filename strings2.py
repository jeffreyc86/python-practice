parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

for char in parrot:
    print(char)

print()

dog = "Pepsi"
for i in range(0, len(dog)):
    print(dog[i])

# negative indexes

print(dog[-2])  # returns s

# slicing
print(parrot[0:7]) # Norwegi

print(dog[1:]) # epsi
print(dog[:4]) #Peps

print(parrot[-7:13])  # an Blu
print(parrot[10:1])     # because ending index is before starting index, an empty str is returned

# slicing with step

dog = "Pepsi is a good dog"
print(dog[2:-2:2]) # pii  odd