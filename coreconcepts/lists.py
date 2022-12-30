names = ['Manu','manu1','manu2','manu3','manu4']
print(names)
print(names[2])
print(names[-2])
print(names[1:4])
#updating a list field
names[0] = 'John'
print(names)

#obtains the highest number
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D lists (array)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#append adds a value to a list
numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)
#insert receives 2 parameters, the index and the value, to insert in a defined position
numbers = [5,2,1,7,4]
numbers.insert(2,25)
print(numbers)
#removes from the list
numbers = [5,2,1,7,4]
numbers.remove(5)
print(numbers)
#prints the position in index of a certain numnber
numbers = [5,2,1,7,4]
print(numbers.index(5))
#sort items ASC or Desc
numbers = [5,2,1,7,4]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
#copy list to another variable
numbers = [5,2,1,7,4]
numbers2 = numbers.copy()
print(numbers2)
#boolean if exists
numbers = [5,2,1,7,4]
print(5 in numbers)
#counts how many times there is a value
numbers = [5,2,1,7,4]
print(numbers.count(5))
#pop removes the last one
numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)
#removes all items in the list
numbers = [5,2,1,7,4]
numbers.clear()
print(numbers)

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


## TUPLES used when the list is not supposed to be modified
#tuples are similar to lists, but we cannot modify them. we cannot change them, add, edit delete, etc.
#list
numbers = [1,2,3]
#tuple
numbers2 = (1,2,3)


#unpacking - unpacks a tuple or list into variables in a single line
coordinates = (1,2,3)

# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
#is the same as writing:unpacking as:
x,y,z = coordinates
print(x,y,z)