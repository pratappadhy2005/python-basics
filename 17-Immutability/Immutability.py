mutable_list = [1, 2, 3]
mutable_list[0] = 5
print(mutable_list)

# Set is mutable
immutable_set = {1, 2, 3}
immutable_set.add(5)
print(immutable_set)

# Dict is mutable
mutable_dict = {"name": "Pratap", "age": 20}
mutable_dict['name'] = 'Sibangi'
print(mutable_dict)


# Tuple is immutable
immutable_list = (1, 2, 3)
# immutable_list[0] = 5
print(immutable_list)

immutable_string = '2343432'
# immutable_string[0] = '5'
print(immutable_string[0])

frozen_set = frozenset({1, 2, 3})
# frozen_set.add(5)
print(frozen_set)


immutable_list = (1, [1, 2, 3], 'word')
# immutable_list[0] = 23
immutable_list[1][0] = 23
print(immutable_list)
