#for will go through each char in the string
for item in 'Python':
    print(item)

#[] creates a list of items
for item in ['Manu','Manu1','Manu2']:
    print(item)

for item in [1,2,3,4,5,6]:
    print(item)

#range will iterate number until a range
for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

#from 5 to 10, jumps by 2
for item in range(5,10,2):
    print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")










