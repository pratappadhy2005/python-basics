print("📢 TEXT CAPITALIZER 📢")
text = input("❓Enter some text:")

print("💀 1. UPPERCASE")
print("💀 2. Lower Case")
print("💀 3. Title Case")
print("💀 4. Sentence Case")

choice = input("❓Enter your choice (1-4): ")

if choice == "1":
    print(text.upper())
elif choice == "2":
    print(text.lower())
elif choice == "3":
    print(text.title())
elif choice == "4":
    print(text.capitalize())
