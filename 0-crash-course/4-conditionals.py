temperature = 20

if temperature > 30:
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
else:
    print("It's cool outside")

# checking multiple conditions with logical operators

age = 18

if age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are not an adult")

# using if statements to check for equality

x = 10
y = 20

if x == y:
    print("x and y are equal")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")
else:
    print("x and y are not equal")

# using if statements to check for membership

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

# ternary operator

x = 10
y = 20

print("x is greater than y") if x > y else print("y is greater than x")
