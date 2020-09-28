class PhoneError(Exception):
    pass
class textNumberError(Exception):
    pass

while True:
    try:
        areaCode = int(input('Enter area code: '))
        if areaCode not in range (100,999):
            raise ValueError
        break
    except ValueError: 
        print('Please only enter number only')
    continue

while True:
    try:
        phoneNumber = int(input('Please enter your phone number: '))        
        if phoneNumber not in range (999999,10000000):
            raise PhoneError
        break
    except PhoneError:
        print('Please enter a valid 7 digit phone number: ')
    continue

while True:
    try:
        numberOfTexts = int(input('Please enter number of texts sent: '))
        
    except:
        print('Please only enter numbers: ')
        continue
    break

bill = 0.0

if numberOfTexts > 100 and numberOfTexts <= 300:
    bill = (numberOfTexts - 100) * 0.03 + 5
elif numberOfTexts > 300:
    bill = (numberOfTexts - 300) * 0.02 + (200 * 0.03) + 5

taxBill = bill*.14 + bill

print('here is the bill before tax ' + '{:.2f}'.format(bill))
print('here is the bill after tax ' + '{:.2f}'.format(taxBill))