num = 1
num1 = 2
num3 = num+num1
print(num3)

print(f"hello {num3}")
test_string="this is a test string"
print(test_string[2:10].upper())


mylist=[1,2,3,4,5,6]
print(mylist[0:2])
mylist.append(num3)
mylist.insert(0,num3)
print(mylist)
item_removed=mylist.pop(0)
print(mylist)
print(item_removed)
mylist.reverse
print(mylist)

#dictionaries
employees = {"1":"manu","2":"manu2","3":"manu3"}
employees["4"] = "manu4"
# employees.items/keys/values
print(employees)

#immutable list
mytuple = (1,2,3)
#comparison operator to return boolean
print(2>3)

a = 23
b = 8
sum = a+b
if sum==42:
    print(sum)
elif sum>30 and sum <41:
    print(sum)
else:
    print(False)

for item in mylist:
    print(item)

a = "*"
for item in mylist:
    a = a +"*"
    print(a)

my_list = []
n = 0
while n < 1000:
    my_list.append(n)
    n = n + 1

print(my_list)


def say_hello():
    print("Hello")


say_hello()


def checker(num):
    if num>100:
        return "greater"
    else:
        return "not greater"

print(checker(810))



def calculator(a,b,operator):
    if(operator=="+"):
        result = a+b
        return result
    else:
        result = a-b
        return result
        
    
print(calculator(2,3,"+"))


class Student():

    planet = "Earth" #class object attribute (no need of self.wont change.)

    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name

student1 = Student(name="manu",last_name="gonzalez")
print(student1.last_name)
print(student1.planet)


class Dog():
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
    
dog1 = Dog(name="Hans",breed="German Shepherd")
dog2 = Dog(name="Lou",breed="Labrador")

print(f"{dog1.name} and {dog2.name} are friends")

class Dog():
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
        
        
    def calculate_human_age(self):
        result = self.age * 7
        return result
        
dog1 = Dog(name = "Hans",breed = "German Shepherd", age = 7)
dog1.calculate_human_age()


class Animal():
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

   
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Cat")
    def sound(self):
        print("meow")
       

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "Dog")
    def sound(self):
        print("ruff")


        
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
#str representation of the object
    def __str__(self):
        return f"{self.title} written by {self.author}"
#length of an object
    def __len__(self):
        return self.pages


mybook = Book("Python","manu",120)
print(mybook)


class Students():
    
    def __init__(self,names):
        self.names = names
    
    def __len__(self):
        return self.names
        
    def __str__(self):
        return f"{self.names}"
        
def useful_func():
    print("useful func")

