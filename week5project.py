class PhoneError(Exception):
    pass
class textNumberError(Exception):
    pass

while True:
    try:
        areaCode = int(input('Please enter your 3 digit area code: '))
        if areaCode not in range (100,999):
            raise ValueError
        break
    except ValueError: 
        print('Only enter a 3 digit number.')
    continue

while True:
    try:
        phoneNumber = int(input('Please enter your 7 digit phone number: '))        
        if phoneNumber not in range (999999,10000000):
            raise PhoneError
        break
    except PhoneError:
        print('Only enter a valid 7 digit phone number.')
    continue

while True:
    try:
        numberOfTexts = int(input('Please enter number of texts sent this month: '))
        
    except:
        print('Only enter numbers. ')
        continue
    break

bill = 5.0

if numberOfTexts > 100 and numberOfTexts <= 300:
    bill = (numberOfTexts - 100) * 0.03 + 5
elif numberOfTexts > 300:
    bill = (numberOfTexts - 300) * 0.02 + (200 * 0.03) + 5

taxBill = bill*.14 + bill


print('The monthly bill for: ')
print('Area Code ' + str(areaCode))
print('Phone number '+ str(phoneNumber))
print('Before tax ' + '{:.2f}'.format(bill))
print('fter tax ' + '{:.2f}'.format(taxBill))