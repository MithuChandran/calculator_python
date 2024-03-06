# Simple Calculator

   This is a simple calculator program written in Python. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division, along with exponentiation. It also includes a history feature that records the details of each calculation performed during the session.
   
## Usage

   To use the calculator:
    
   1.Clone the repository to your local machine.
   2.Run the calculator.py script.
   3.Follow the prompts to enter numbers, choose an operation, and view the result.
   4.Optionally, view the calculation history at the end of the session.

## Features
   - Addition, subtraction, multiplication, division, exponentiation operations.
   - Input validation to handle errors gracefully.
   - Calculation history display.

## Error Handling

   The calculator handles the following errors:

    - If you enter a non-numeric value for the numbers, it will raise a `ValueError`.
    - If you try to divide by zero, it will raise a `ZeroDivisionError`.
    - If any other error occurs, it will display an error message.

 ## Calculation History

   The calculator keeps track of the calculations you perform and displays them at the end. Each calculation is stored as a tuple containing the first number, second number, operation, and result.
