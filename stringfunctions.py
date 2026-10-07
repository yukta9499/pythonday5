text = " hello, I am Yukta Kale! "

#strip spaces from both ends
print("Remove Spaces",text.strip())
#convert to uppercase
print("Upper Case:", text.upper())

#capitalize first letter
text = text.strip()
print("Capitalize First Letter :", text.capitalize())

#Title case
print(text.title())

#count occurences of a substring
print("Letter C occurs", text.count("Y"),"times in text")

#Find the position of the substring(-1 if not found)
print("Position of Yukta in text is",text.find("Yukta"))

#Replace a substring
print(text.replace("Yukta","Yukkss"))


