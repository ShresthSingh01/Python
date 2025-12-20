#sets=Sets are used to store multiple items in a single variable.

#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

#A set is a collection which is unordered, unchangeable*, and unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)

print(len(thisset))

print(type(thisset))

#Using the set() constructor to make a set
thisset1 = set(("apple", "banana", "cherry")) #note the double round-brackets
print(thisset1)     

#Access Items
for x in thisset:
    print(x)
#Check if "banana" is present in the set
print("banana" in thisset)
#Add Items
thisset.add("orange")
print(thisset)
#Add Multiple Items
thisset.update(["mango", "grapes", "pineapple"])
print(thisset)
#Remove Item
thisset.remove("banana") #will raise an error if the item to remove does not exist
print(thisset)
thisset.discard("apple") #will NOT raise an error if the item to remove does not exist
print(thisset)
#Remove Last Item
x = thisset.pop() #removes a random item
print(x)