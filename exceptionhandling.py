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

#types of exceptions
#1. IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")
#2. KeyError
my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError:
    print("Error: Key not found in dictionary.")
#3. TypeError
try:
    result = '2' + str(2)
except TypeError:
    print("Error: Unsupported operand type(s) for +.")
#4. AttributeError
my_string = "Hello"
try:
    my_string.append(' World')  # This will raise AttributeError since strings don't have append()
except AttributeError:
    print("Error: 'str' object has no attribute 'append'.")
#5. ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid literal for int() with base 10.")

#6. FileNotFoundError
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()   
except FileNotFoundError:
    print("Error: File not found.")