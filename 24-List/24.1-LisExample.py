myList = [1,2.3,4,5,6,7,8,9,10]
print(myList)

print("================")

myList2 = list()
print(myList2)

print("================")

myList2.append(1)   
print(myList2)

print("================")

myList3 = [4,5,7,'Apple','Pineapple','Oranage','Grape','Mango']
item = myList3[3]
print(item)
print(myList3[-2])

print("================")

for item in myList3:
    print(item)

print("================")

if item in myList3:
    print('Item is in the list')
else:
    print('Item is not in the list')

print("================")

print(len(myList3))

myList3.insert(3,'Banana')
print(myList3)

myList3.pop()
print(myList3)

myList3.remove('Apple')
print(myList3)

myList3.reverse()
print(myList3)

myList4 = [1,2,3,4,200,202,505,5,6,7,8,9,10]
myList4.sort()
print(myList4)

myList5 = [0] * 5
print(myList5)

myList6 = myList4 + myList5
print(myList6)

myList7 = [1,2,3,4,5,6,7,8,9,10]
a = myList7[1:5]
print(a)

b= myList7[2:]
print(b)
c = myList7[:5]
print(c)
d = myList7[1::3]
print(d)

print("================")

list_org = ["banana", "cherry", "apple", "kiwi", "mango", "pear"]
list_copy = list_org.copy()
list_copy.sort()
print(list_copy)
print(list_org)

print("================")

list_nest_orig = [["banana", "cherry", "apple"], ["kiwi", "mango", "pear"], ["orange", "watermelon", "grapes"]]
list_nest_copy = list_nest_orig.copy()
list_nest_copy[0][0] = "lemon"
print(list_nest_copy)
print(list_nest_orig)

print("================")
#List comp
mylist_comp = [1,2,3,4,4,5,6,7,8,9,10]
comp_list = [i*i for i in mylist_comp if i % 2 == 0]
print(comp_list)