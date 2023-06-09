course = "Python's course for beginners"
# use double "" when using ' in the middle of the string
print(course)

course = 'Python for "Beginners"'
print(course)

#multi line string
course = '''
 Hi Manu
 Thank you for learning python.
 Have a good day.
 Regards,
 Manu
 '''
print(course)

#print only x character in a string
course = "Python's course for beginners"
print(course[0])
#to start from the end use negative "-"
print(course[-1])
#to print a row of characters (0 1 2 3) wont inclue the '3' byte
course = "Python's course for beginners"
print(course[0:3])
#print the whole string starting at 0
print(course[0:])
#print the whole string starting at X
print(course[4:])
#print assuming it starts at 0 but ends at X
print(course[:5])

#saves string into another variable defining which characters : assumes 0 to end if not defined.
course = 'Python for beginners'
another = course[:]
print(another)

#excludes the first and last characters from the string
name= 'Jennifer'
print(name[1:-1])

#formatted string instead of multiple strings
first = 'Manuel'
last = 'Gonzalez'
#multiple strings
# message = first + ' ['+last+'] is a coder'
#formatted string
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'
#counts the total characters len(). used to limit the length of an input
print(len(course))
#set al letter CAP
print(course.upper())
#original variable is not changed
print(course)
#find the first index of a letter in a string
print(course.find('P'))
#replace a word or string for another
print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('P','J'))
#find if a string is contained within a variable - returns boolean
print('Python' in course)

























































































































































