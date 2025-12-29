#Inheritance= A mechanism in OOP that allows a new class (derived class) to inherit properties and behaviors (attributes and methods) from an existing class (base class). This promotes code reusability and establishes a hierarchical relationship between classes.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!


#Polymorphism= The ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.
class Bird:
    def speak(self):
        return "Chirp!"
def animal_sound(animal):
    print(animal.speak())
bird = Bird()
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(bird)  # Output: Chirp!






#Encapsulation= The bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300


#Polymorphism with Inheritance
class Vehicle:
    def start_engine(self):
        return "Engine started"
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with a roar!"
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started with a vroom!"
def vehicle_start(vehicle):
    print(vehicle.start_engine())
car = Car()
motorcycle = Motorcycle()   
vehicle_start(car)          # Output: Car engine started with a roar!
vehicle_start(motorcycle)   # Output: Motorcycle engine started with a vroom!
#Encapsulation with Getters and Setters
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
person = Person("shresth", 30)
print(person.get_name())  # Output: shresth