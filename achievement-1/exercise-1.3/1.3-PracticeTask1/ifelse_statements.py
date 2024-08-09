number1 = input('First number:')
number2 = input('Second number:')
operator = input('Operator:')

if operator == '+':
    result = float(number1) + float(number2)
elif operator == '-':
    result = float(number1) - float(number2)
else:
    print('Unknown Operator')

print(number1, operator, number2, 'is', result)