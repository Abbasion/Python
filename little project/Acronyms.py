user_input = str(input("Enter the Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a +str(i[1]).upper()
print(a)