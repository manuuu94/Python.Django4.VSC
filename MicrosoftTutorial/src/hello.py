from datetime import date

print('Hello World')


distance = 5
type(distance)
print(2-1)

x=2
x *= 2
x /= 2
x += 2
x -= 2
print(x)


print("Today's date is: " + str(date.today()))


parsecs=11
lightyears = parsecs * 3.26

print(f"{parsecs} parsecs is {lightyears} lightyears")


print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)


print("""Both sides of the %s get the same amount of sunlight,
... but only one side is seen from %s because
... the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))





planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
planet.update({'name': 'Makemake'})
planet['name'] = 'Makemake'

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79


planet['orbital period'] = 4333

planet.pop('orbital period')

planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}


for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')



def variable_length(*args):
    print(args)

#It isn't required to call variable arguments args. 
# You can use any valid variable name. Although it's common to see *args or *a, you should try to use the same convention throughout a project.


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    

print(sequence_time(4, 14, 18))
'Total time to launch is 36 minutes'  



def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}















