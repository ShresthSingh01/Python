#class= is  like a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

del p1
#The __init__() Function
class Person0:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person0("John", 36)
print(p1.name)
print(p1.age)
#Object Methods
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person1("John", 36)
p1.myfunc()
#The self Parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()


#You can create multiple objects/instances of the same class:

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Person2:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person2("Abby")
p2 = Person2("Lins")

p1.printname()
p2.printname()

#Access properties
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)
#Modify properties
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person3("Abby", 25)
print(p1.age)

p1.age = 26
print(p1.age)
