#if applicant has high income AND good credit
#   Eligible for loan
high_income = True
good_credit = True
criminal_record = False

if high_income and good_credit:
    print("Eligible for loan")

if high_income or good_credit:
    print("Eligible for loan")

#not operator changes the boolean value
if good_credit and not criminal_record:
    print("Eligible for loan")