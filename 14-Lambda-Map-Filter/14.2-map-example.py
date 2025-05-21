from functools import reduce
list_temp = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, list_temp))
print(result)

list_filter = list(filter(lambda x: x % 2 == 0, list_temp))
print(list_filter)


list_reduce = reduce(lambda x, y: x + y, list_temp)
print(list_reduce)
