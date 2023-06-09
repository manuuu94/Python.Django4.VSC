try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

#allows to use multiple exceptions

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")


