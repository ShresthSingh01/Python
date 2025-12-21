#range = The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

#This set of numbers has its own data type called range.

#Using the range() function
'''for x in range(6):
    print(x)

x = range(10)
print(x)
for n in x:
    print(n)
    print(list(x))
    break


x1 = range(3, 10)
for n in x1:
    print(n)
    print(list(x1))
    break'''
    
x2 = range(3, 10, 2)
for n in x2:
    print(n)
    print(list(x2))
    break

#slice the range
r = range(10)
print(r[2])
print(r[:3])
print(r[2:5])
print(r[::2])
print(r[::-1])

#membership test
print(5 in r)
print(15 in r)
print(15 not in r)

#using len() function
print(len(r))
#using min() and max() functions
print(min(r))
print(max(r))
#using sum() function
print(sum(r))