print("VOWEL COUNTER")

input_vowel = input("Enter a word: ")


def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for letter in word if letter in vowels)


print(f"Number of vowels in {input_vowel} is {count_vowels(input_vowel)}")
