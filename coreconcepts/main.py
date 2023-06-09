# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import datetime
import re
import sys


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


try:
    [1,2,3][4]
except IndexError:
    print("IndexError Raised")
except:
    print("Exception Raised")
else:
    print("Else")
finally:
    print("Clean")

a=7
print(a.__str__())





print(set([1,2,1]) == set([1,2]))

a = {1:9,2:8,3:7,4:6,5:5}
print(a.get(6))

def f():
    return 42
    f()
    

print(f())


print("Hello" 'world' * 2)





class test():
    id = 0
    def __init__(self,id):
        self.id=id
        id=2

t = test(1)
print(t.id)


m = re.search(r'(ab[cd]?)',""""acdeabdabcde""""")

print(m.groups())

print(sys.path)


type(datetime.date(2012,01,01)-datetime.date(2011,01,01))