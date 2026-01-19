name=input("Enter a name: ")
text=name.lower()
if(text[::-1]==name):
    print("Given name is palindrom")
else:
    print("Not a palindrom")

