# Without comprehension
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

# List Comprehension
square2 = [i**2 for i in range(10) if i > 5 and i % 2 == 0]
print(square2)
