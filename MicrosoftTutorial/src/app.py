from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)


planets = [10]
new_planet = ""
user_input = input("Desea añadir otro planeta ")
while user_input=="Y":
    new_planet=input("Digite un planeta ")
    planets.append(new_planet)
    user_input = input("Desea añadir otro planeta ")


print(planets)

