#classes are used to define new types or objetcs - numbers, strings, boolean - lists - dictionaries - methods
#when naming clasess, you only capitalize the first letter of every word, no underscore
class Point:
    def __init__(self,x,y):
        ##uses self to reference the same object and self to refer to its variable x
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

##constructor to use
point = Point(10,20)
print(point.x)

point1 = Point()
point1.draw()
point1.move()

#constructor is a function that gets called at the time of creating an object. parameters.

class Person:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
        
    def talk(self):
        print(f"Hi, I am {self.name} {self.last_name}")

    
    def __str__(self):
        return f"{self.name} {self.last_name}. this is the str of the object, if you want to print it. Otherwise, you get only it's space in memry"



manu = Person("Manu","Gonzalez")
manu.talk()
print(manu)

#inheritance is a way to reuse code - dont repeat youself


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass  #inheritance is a way to reuse code - dont repeat youself


class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()






