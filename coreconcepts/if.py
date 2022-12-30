is_hot=True
is_cold=False

#open indent and executes if TRUE, otherwise FALSE it continues
#true will print both values, the one in indent and the other outside the indent. false will only print the second one outside the indent. shift tab to getout the if or else
if is_hot:
    print("Its a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
print("Enjoy your day")

#Price of a house is $1M. If buyer has good credit,
#they need to put down 10%
#otherwise
#they need to put down 20%
#Print down the payment
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")