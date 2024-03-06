def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def exponentiate(x, y):
    return x ** y

def calculator():
    history = []  # Initialize an empty list to store history
    
    while True:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            operation = input("Enter operation (+, -, *, /, ^, **): ")

            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '^':
                result = exponentiate(num1, num2)
            elif operation == '**':
                result = exponentiate(num1, num2)
            else:
                print("Invalid operation!")
                continue
            
            print("Result:", result)
            history.append((num1, num2, operation, result))  # Append the calculation to history
            
            
        
        except ValueError as ve:
            print("Error:", ve)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print("An error occurred:", e)
    
    

