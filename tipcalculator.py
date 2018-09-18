totalAmount = int(input('Enter total amount: '))
percentage = int(input('Enter tip % amount: '))

def tipCalculator():
    print( totalAmount * (percentage / 100))

tipCalculator()
