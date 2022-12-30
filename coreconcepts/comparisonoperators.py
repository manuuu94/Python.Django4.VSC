temperature = 33

if temperature > 30:
    print("its a hot day")
else:
    print("its not a hot day")


# < > <= >= == !=

name = "ma"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

#exercise:
#inputs weight and if its in (L)bs or anything else, then converts it to the other measure type.
weight = int(input('Weight?: '))
unit = input('(L)bs or (K)g; ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")