print("NAME GENERATOR")

first_names = ["John", "Jane", "Michael", "Emily", "David",
               "Sarah", "Robert", "Emma", "William", "Olivia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

names_count = input("How many names do you want to generate?")

for i in range(int(names_count)):
    if i >= len(first_names):
        break
    print(f"{first_names[i]} {last_names[i]}")
