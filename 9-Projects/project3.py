# for i in range(1, 10, 3):
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers.append(11)
# print(numbers[2])
# print(len(numbers)-1)

# numbers.pop(2)
# print(numbers)

fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")

for fruit in fruits:
    print(fruit)

for fruit in range(len(fruits)):
    print(fruit)

names = []
ages = []
emails = []

name = input("Name: ")
age = input("Age: ")
email = input("Email: ")

names.append(name)
ages.append(age)
emails.append(email)

print(names)
print(age)
print(email)
