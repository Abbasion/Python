import random
import string
print("Generate a random alphabatical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate a random alphabatical string:")
max_length = 255
str1 = ""
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)
print("\n generate a random alphabatical string of a fixed length: ")
str1 = ""
for i in range(10):
    str1 += random.choice(string.ascii_letters)
print(str1)
