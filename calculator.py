import re


def simple_calculator():
    while True:
        a = ask_for_input("Please provide a number: ", is_number)
        if a is None:
            break
        print(a)
        op = ask_for_input("Please provide an operator (+, -, *, /): ", is_valid_operator)
        if op is None:
            break
        print(op)
        b = ask_for_input("Please provide another number: ", is_number)
        print(b)
        result = calc(op, convert_number(a), convert_number(b))
        print(f"{a} {op} {b} = {result}")


def ask_for_input(prompt, validation_func):
    while True:
        inp = input(prompt)
        if validation_func(inp):
            return inp
        print("Invalid input, try again.")


def is_number(string):
    return bool(re.match(r"^-?\d+(\.\d+)?$", string))


def convert_number(string):
    try:
        return int(string)
    except ValueError:
        return float(string)


def is_valid_operator(operator):
    return operator in ['+', '-', '*', '/']


def calc(operator, a, b):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None
    }
    if operator not in operations:
        print("Error: Unknown operator")
        return None
    if operator == '/' and b == 0:
        print("Error: Division by zero")
        return None
    try:
        result = operations[operator](a, b)
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    return result


if __name__ == '__main__':
    simple_calculator()
