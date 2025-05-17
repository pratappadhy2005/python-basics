print("🔍 Website Checker 🔍")
url = input("Enter the website url: ")
if url.__contains__("https"):
    print("The website is secure")
elif url.__contains__("http"):
    print("This website is based on http") 
else:
    print("This website is not secure")