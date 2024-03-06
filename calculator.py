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
            
            while True:
                choice = input("Do you want to perform another calculation? (yes/no): ").lower()
                if choice in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
            
            if choice == 'no':
                print("Thank You for Using the Calculator!!!")
                break
        
        except ValueError as ve:
            print("Error:", ve)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print("An error occurred:", e)
    
    # Display history
    print("\nCalculation History:")
    for index, calc in enumerate(history, start=1):
        num1, num2, operation, result = calc
        print(f"{index}. {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
