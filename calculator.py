def is_number(str):
    try:
        if str == "0":
            raise ValueError
        float(str)
        return True
    except ValueError:
        return False


def convert_number(str):
    return float(str)


def is_valid_operator(operator):
    return operator in ['+', '-', '*', '/']


def ask_for_a_number(force_valid_input):
    while True:
        inp = input("Please provide a number: ")
        if is_number(inp):
            return float(inp)
        else:
            if not force_valid_input:
                print("This didn't look like a number, try again.")
                return None


def ask_for_an_operator(force_valid_input):
    while True:
        operation = input("Please provide an operation (one of +, -, *, /): ")
        if is_valid_operator(operation):
            return operation
        if not force_valid_input:
            print("Unknown operation.")
            return None


def calc(operator, a, b):
    if not is_valid_operator(operator) or not is_number(a) or not is_number(b):
        return None
    result = None
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b != 0:
            result = a / b
        else:
            print("Error: Division by zero")
    return result


def simple_calculator():
    while True:
        a = ask_for_a_number(force_valid_input=False)
        if not a:
            break
        op = ask_for_an_operator(force_valid_input=True)
        b = ask_for_a_number(force_valid_input=True)
        result = calc(op, a, b)
        if result:
            print(f"The result is {calc(op, a, b)}")


if __name__ == '__main__':
    simple_calculator()
