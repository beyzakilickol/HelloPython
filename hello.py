#FUNCTIONS OR METHODS
def greet():
    print('I am inside of the function')

greet()

def greet(name,age):
    print('Hello, ' + name)

greet('John',32)

def add(firstNumber , secondNumber):
    return firstNumber + secondNumber #anything after return line will be ignored!

#result = add(2,4) #is the sama as print(add(2,4))
#print(result)

#CONDITIONS
if(1 == 1):
    print('equal')
    a = 10
    b = 10
    c = a + b
else:
    print('not equal')

def evenOrOdd(number):

    if(number % 2 == 0):
        print('Even')
    else:
        print('odd')

evenOrOdd(5)
age = int(input('enter age:'))
def validate_age():
    if(age >= 18):
        print('age is greater than or equal to 18')
    elif(age < 13):
        print('age is less than 13')
    else:
        print('age is not greater than 18 and not less than 13')

validate_age()






























#string concatenation
#message = "Hello " + 'World' + 'And' + 'Year'

#print(message)
#firstName = input('Enter first name: ')
#lastName = input('Enter last name: ')
#message = firstName + ', '+ lastName
#print(message)
#city = input('Enter City: ')
#state = input('Enter State: ')
#zipCode = input('Enter Zip Code: ')

#message = 'My name is ' + firstName + ', ' + lastName + ' and I live in '+ city + ', ' + state + ' ' + zipCode
#shortway to do this
#message = 'My name is {0}, {1} and I live in {2}, {3} {4}'.format(firstName,lastName, city, state, zipCode)
#print(message)


# snake case = first_number
#camel case = first_number
#first_number = input("Enter first number: ")

#second_number = input("Enter second number: ")
#result = int(first_number) + int(second_number)
#print(result)
#number= int('45')
#first_number_as_int = int('45')
#second_number_as_int = int('70')
#some_result = first_number_as_int + second_number_as_int
#print(some_result)
#print(result)
# input function always return to string data
#a = 10 # integer
#b = "hello" # string
#c = 10.45 #float
#d = True # boolen
#first_number = float(input("Enter first number: "))

#second_number = float(input("Enter second number: "))
#result = int(first_number) + int(second_number)
##float function converts to decimal
#firstNumber = int (input ('Enter the first number:'))
#secondNumber = int (input ('Enter the second number:'))
#thirdNumber = int (input ('Enter the third number:'))
#result2 = firstNumber + secondNumber + thirdNumber
#print(result2)
