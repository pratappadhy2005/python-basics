print("CHARACTER CHECK TYPE")

char = input("Enter a single character: ")

if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")
