import math
x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)

print("================")
x += 15
print(x)

x -= 15
print(x)

x *= 15
print(x)

print("================")

# String Operations
first = "John"
last = "Doe"
full = first + " " + last
print(full)

print("Hey my name is " + first + " and my last name is " + last)
print(f"Hey my name is {first} and my last name is {last}")


# int floor division
a = 10
b = 3
print(a // b)

# float division
print(a / b)

print("================")

i, j, k = 1, 2, 3
print(i, j, k)

print("================")

# swap values

m = 10
n = 20

m, n = n, m
print(m, n)

print("================")

# comparison operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("================")

# logical operators

a = True
b = False

print(a and b)
print(a or b)
print(not a)

print("================")

# String slicing

s = "Hello, World!"

print(s[0])
print(s[0:5])
print(s[0:5:2])
print(s[::2])
print(s[::-1])

print("================")

# String formatting

name = "John"
age = 25

print("Hello, my name is {} and I am {} years old" .format(name, age))

print("================")

# Membership operators

s = "Hello, World!"

print("H" in s)
print("h" in s)
print("H" not in s)
print("h" not in s)

print("================")

# Using placeholders

name = "John"
age = 25

print("Hello, my name is %s and I am %d years old" % (name, age))

print("================")

# Math module operations

print(math.pi)
print(math.sqrt(16))
print(math.ceil(2.3))
print(math.floor(2.3))
print(math.pow(2, 3))
print(math.factorial(5))
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(0))
