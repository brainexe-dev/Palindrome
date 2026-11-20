text = "madam"
clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")