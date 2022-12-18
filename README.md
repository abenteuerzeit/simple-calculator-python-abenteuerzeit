# Simple Calculator

This is a simple command-line calculator implemented in Python 3. The calculator prompts the user to enter two numbers and an operator (e.g. +, -, *, /), performs the specified operation on the numbers, and prints the result. The calculator continues to run until the user enters a non-numeric value for the first number.

## Requirements

This calculator requires Python 3.

## Usage

To use the calculator, clone or download the repository and run the main.py script:

```console
git clone https://github.com/CodecoolGlobal/simple-calculator-python-abenteuerzeit.git
cd simple-calculator-python-abenteuerzeit
python3 calculator.py
```

The calculator will then prompt you to enter two numbers and an operator:

```console
Please provide a number: 5
Please provide an operator (one of +, -, *, /): *
Please provide a number: 7
Result: 35
```

The calculator will continue to run until you enter a non-numeric value for the first number:

```console
Please provide a number: hello
```

## Implementation Details

The calculator is implemented in the calculator.py script and consists of several helper functions:

- is_number(string): Returns True if the string can be converted to a numeric value (int or float), False otherwise.
- convert_number(string): Converts the string to a numeric value (int or float).
- ask_for_a_number(force_valid_input=False): Asks the user for input and returns the numeric value of the input string. If force_valid_input is True, the function will continue to ask for input until the input is a valid number. If force_valid_input is False and the input is not a valid number, the function will return None.
- is_valid_operator(operator): Returns True if the operator is one of +, -, *, /, False otherwise.
- ask_for_an_operator(force_valid_input=False): Asks the user for input and returns the operator if the input is valid. If force_valid_input is True, the function will continue to ask for input until the input is a valid operator. If force_valid_input is False and the input is not a valid operator, the function will return None.
- calculate(number1, operator, number2): Performs the operation specified by the operator on the two numbers and returns the result.

The calculator is designed to be run in a loop, where each iteration prompts the user for two numbers and an operator and performs the specified operation. If an invalid value is entered for the first number, the loop is broken and the calculator exits.
