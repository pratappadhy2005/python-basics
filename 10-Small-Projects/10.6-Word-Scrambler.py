print("WORD SCRAMBLER")

while True:
    word = input("Enter a word: ")
    if word == "exit":
        break
    else:
        print(word[2:] + word[0:2])
