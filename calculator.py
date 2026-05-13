# python program for basic calculator 
def addition(num1, num2): # adding two number
    return num1+num2
def subtraction(num1, num2): # subtracting two number
    return num1-num2
def multiplication(num1, num2): # multiplying two number
    return num1*num2
def division(num1, num2): # dividing two number
    if num2==0:
        return 'Cannot divide by zero'
    return num1/num2
def average(num1, num2): # average of two number
    return (num1+num2)/2
print('Choose one of the operation given below to see your answer :\n1. Addition \n2. Substraction \n3. Multiplication \n4. Devision \n5. Average')
operation=int(input())
if operation in [1, 2, 3, 4, 5]:
    number1 =float(input('Enter first number: '))
    number2 =float(input('Enter second number: '))
    if operation==1:
        print('Addition of two number is num1 + num2 =', addition(number1, number2))
    elif operation==2:
        print('Subtraction of two number is num1 - num2 =', subtraction(number1, number2))
    elif operation==3:
        print('Multiplication of two number is num1 * num2 =', multiplication(number1, number2))
    elif operation==4:
        print('Division of two number is num1 / num2 =', division(number1, number2))
    elif operation==5:
        print('Average of two number is ( num1 + num2 ) / 2 =', average(number1, number2))
else:
    print('This operation is not avaliable at this moment please enter another operation.')
