myTuple = (1,2,3,4,5,6,7,8,9,10)
print(myTuple)
print("================")

print(myTuple[1:5])
print("================")

for i in myTuple:
    print(i)
print("================")

myTuple1 = ("mytuple")
print(type(myTuple))
print("================")

myTuple2 = (["Pratap", "Kumar"])
print(myTuple2)
print("================")

if "Pratap" in myTuple2:
    print("It's my tuple")
print("================")

print(myTuple2[0])
print("================")

print(len(myTuple))
print("================")
print(myTuple.count(1))

print("================")
print(myTuple.index(1))

print("================")
my_list = list(myTuple)
print(my_list)

print("================")