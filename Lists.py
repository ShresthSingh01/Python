'''#list=Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:'''
'''thislist = ["apple", "banana", "cherry"]
print(thislist)
#Accessing List Items
print(thislist[0])
print(thislist[1:3])
#Duplicates are allowed
thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist1)
#List Length
thislist2 = ["apple", "banana", "cherry"]   
print(len(thislist2))  
#List Items - Data Types
list1 = ["apple", "banana", "cherry"]        
list2 = [1, 5, 7, 9, 3]             
list3 = [True, False, False]    
list4 = ["abc", 34, True, 40.6]
print(list1)
print(list2)
print(list3)
print(list4)'''
#check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Change Item Value
thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = "blackcurrant"
print(thislist1)
#Change a Range of Item Values
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)
#Insert Items
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")   
print(thislist3)
#Append Items
thislist4 = ["apple", "banana", "cherry"]
thislist4.append("orange")
print(thislist4)