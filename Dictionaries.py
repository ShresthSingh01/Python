#Dictionary=Dictionaries are used to store data values in key:value pairs.  
#Dictionaries are one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Set, all with different qualities and usage.
thisdict= {
    "class":"V",
    "section":"A",
    "rollno":12
}
print(thisdict)
print(len(thisdict))

#using dict() constructor to make dictionary
thisdict1 = dict(name="John", age=36, country="Norway")
print(thisdict1)

#Accessing Items
thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict2["model"]
print(x)
y = thisdict2.get("model")
print(y)

#Get Keys
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x=car.keys()
print(x)
car["color"] = "white"
print(x)
#Get Values
z=car.values()
print(z)

#check if key exists
thisdict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict3:
    print("Yes, 'model' is one of the keys in the thisdict3 dictionary")
    