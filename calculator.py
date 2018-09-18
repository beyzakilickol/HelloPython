input1 = int(input('Enter first number: '))
input2 = input('Enter the operand (+, -, *, /): ')
input3 = int(input('Enter first number: '))

def calculator():
    if(input2 == '+'):
        print(input1 + input3)
    elif(input2 == '-'):
        print(input1 - input3)
    elif(input2 == '*'):
        print(input1 * input3)
    elif(input2 == '/'):
        print(input1 / input3)
    else:
        print('undefined')

calculator()
