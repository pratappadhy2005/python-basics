name = input("Enter your name: ")

print("Hello, " + name + "!")

age = input("Enter your age: ")

print("You are " + age + " years old")

years_to_retirement = 65 - int(age)

print("You will retire in " + str(years_to_retirement) + " years")

# Working with multiple input values
x, y = input("Enter two values: ").split()
print(f"x: {x}, y: {y}")


user_choice = input("Enter a color: ")
if user_choice == "red":
    print("I like red too!")
elif user_choice == "blue":
    print("Blue is a nice color!")
else:
    print("I don't like that color!")
