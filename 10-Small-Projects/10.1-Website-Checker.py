print("🔍 Website Checker 🔍")
website_name = input("Enter the website url: ")
if website_name.__contains__("https"):
    print("The website is secure")
elif website_name.__contains__("http"):
    print("This website is based on http") 
else:
    print("This website is not secure")