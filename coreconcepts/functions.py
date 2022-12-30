#reserve keyword for defining a function , followd by function name (): which means block of code, indente (tab)
def greet_user():
    print("Hi There!")
    print("Welcome aboard")


#execution starts here, because function is not called, only defined.


print("Start")
greet_user()
print("Finish")


##parameters are the placeholders we define in our function for receiving information. arguments are the actual piece of information that is supplied.
nombre = input('nombre?')
def greet(nombre):
    print("Hi there " + nombre)


greet(nombre)

##using keyword argument in parameters
def greet2(nombre,edad):
    print(f"Su nombre es {nombre} y tiene {edad}")

#se usan para que los parametros no se preocupen por el orden de los argumentos.
greet2(edad = 18, nombre = "Manu")
#if mixing, you should use the position argumennts first, then the keyword arguments.


##return - if there´s no return the none value is returned by default
def sqr(number):
    return number * number


#may store in variable or just print the function
print(sqr(3))



