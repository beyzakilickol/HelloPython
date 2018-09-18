number = int(input('Enter your number: '))

def evenOrOdd():
    if(number % 2 == 0):
        print('even')
    elif(number % 2 == 1):
        print('odd')
    else:
        print('neither')

evenOrOdd()
