num1 = float(input('First number: '))
operator = input('Operator: ')
num2 = float(input('Second number: '))


def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Not supported!"


print(calculate(num1, num2, operator))
