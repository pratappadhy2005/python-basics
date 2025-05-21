print("📑 MUSIC RECOMMENDER 📑")

input_genre = input("What genre do you lie? rock/pop/hip-hop?")

if input_genre == "rock":
    print("You might like The Beatles")
elif input_genre == "pop":
    print("You might like Taylor Swift")
elif input_genre == "hip-hop":
    print("You might like Kendrick Lamar")
else:
    print("I don't know that genre")
