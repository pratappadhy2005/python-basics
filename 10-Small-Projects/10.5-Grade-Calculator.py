print("GRADE CALCULATOR")

total_score = 0
counter = 0

while True:
    score = input("Enter a score (or 'Done' to quit): ")
    if score == "Done":
        break
    total_score += float(score)
    counter += 1
    average_score = total_score / counter
    if average_score > 90:
        print("Grade: A")
    elif average_score > 80:
        print("Grade: B")
    elif average_score > 70:
        print("Grade: C")
    elif average_score > 60:
        print("Grade: D")
    else:
        print("Grade: F")
