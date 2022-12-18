# Simple Calculator

This is a simple calculator that can perform basic arithmetic operations.

## Usage

To use the calculator, run the simple_calculator function. The calculator will prompt the user to enter two numbers and an operator, and will then perform the specified operation on the numbers. The following operators are supported:

+: addition
-: subtraction
*: multiplication
/: division
The calculator will continue to run until the user inputs None for one of the numbers or the operator.

## Validation

The calculator includes several validation checks to ensure that the input is valid. The is_number function is used to validate that the input is a number, and the is_valid_operator function is used to validate that the input is a supported operator. If the input is not valid, the user will be prompted to try again.

## Error Handling

The calculator also includes error handling for division by zero errors. If the user attempts to divide by zero, the calculator will display an error message and return None as the result.

## Testing

The calculator includes a test suite in the tests.py file. To run the tests, simply run the unittest module on the Tester class. The tests cover all of the main functionality of the calculator, including validation and error handling.

## Dependencies

The calculator relies on the re module for input validation. This module is part of the Python standard library and does not need to be installed separately.
