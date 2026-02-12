#Using Multiple assignment 
a = [10, 20, 30, 40, 50]
a[0], a[4] = a[4], a[0]

print(a)
#Using XOR
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
#Using temp 
a = [10, 20, 30, 40, 50]

temp = a[2]
a[2] = a[4]
a[4] = temp
print(a)