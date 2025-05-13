print("Hello, World!")

# Case sensitive language

# Strings
name = "John"

# Integer
age = 25

# Float
price = 19.5

# Boolean
is_published = True

# None
is_published = None

print("Name:", name)
print("Age:", age)
print("Price:", price)
print("Is published:", is_published)
print(name[-1])

message = "Hello, World!"
print(message.lower())
print(message.capitalize())
print(message.replace("Hello", "Hi"))
print("World" in message)
print(len(message))

greeting1 = "Hello"
greeting2 = "hellow"

if greeting1 == greeting2:
    print("They are the same")
else:
    print("They are not the same")


# Type Conversion
age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))


price_float = 10.95
price_int = int(price_float)
print(price_int)
