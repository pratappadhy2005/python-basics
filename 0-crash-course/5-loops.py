# For loops
for i in range(5):
    print(i)

print("\n Reverse Continuing")
for i in range(5, 0, -1):
    print(i)

print("\n Continue with a step")
for i in range(0, 10, 2):
    print(i)

# while loops
i = 0
while i < 5:
    print(i)
    i += 1

# break and continue
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n Continue")
for i in range(10):
    if i == 5:
        continue
    print(i)

# Looing through a collection
names = ["John", "Jane", "Jim", "Jill"]
for name in names:
    print(name)

# reversing a list
names.reverse()
for name in names:
    print(name)

# loop with enumerate
for index, name in enumerate(names):
    print(index, name)

# loop with dictionary
person = {"name": "John", "age": 20, "city": "New York"}
for key, value in person.items():
    print(key, value)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# For loop with zip
names = ["John", "Jane", "Jim", "Jill"]
ages = [20, 21, 22, 23]
for name, age in zip(names, ages):
    print(name, age)

# infinite loop with break
while True:
    print("Hello")
    break

# infinite loop with continue
while True:
    print("Hello")
    continue

# infinite loop with break and continue
