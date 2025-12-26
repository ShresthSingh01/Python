#Functions=A function is a block of code which only runs when it is called.

#A function can return data as a result.

#A function helps avoiding code repetition.


#creating a function
def my_function():
  print("Hello from a function")

#calling a function
my_function()
#function with parameters
def greet(name):
    print("Hello, " + name + "!")
greet("Shresth")
greet("Tony")
#function with return value
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)
#function with default parameter value
def greet_with_default(name="Guest"):
    print("Hello, " + name + "!")
greet_with_default()
greet_with_default("Tony")
#function with multiple parameters
def multiply(x, y):
    return x * y
product = multiply(4, 5)
print("The product is:", product)
#function with keyword arguments
def describe_person(name, age):
    print("Name:", name)
    print("Age:", age)
describe_person(age=30, name="Alice")
#function with variable-length arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
total_sum = sum_all(1, 2, 3, 4, 5)
print("The total sum is:", total_sum)
#function with docstring
def square(num):
    """Returns the square of a number."""
    return num * num
print("The square of 4 is:", square(4))
print(square.__doc__)