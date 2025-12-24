# Exception Handling in Python = The try block lets you test a block of code for errors.

'''The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.'''

try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")

