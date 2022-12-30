import random

class Dice:
    def roll(self):
        first =random.randint(1,6)
        second = random.randint(1,6)
        return first,second


dice = Dice()
print(dice.roll())


#modules
for i in range(3):
    print(random.random())
    print(random.randint(10,20))


members = ["John","Mary","Mosh"]
leader = random.choice(members)
print(leader)

#3:42:24