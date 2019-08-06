# String Manipulation
import string
import Solution

# print("Hello World")

fruit = 'banana'

# letter = fruit[1]

# print(letter)
# x = len(fruit)
# print(x)

index = 0

# while index < len(fruit):
#     letter = fruit[index]
#     print(index, " ", letter)
#     index = index + 1
#
# for letter in fruit:
#     print(letter)

count = 0

for letter in fruit:
    if letter == 'a':
        count += 1
print(count)

s = 'Monty Python'

# string slicing in python

print(s[0:5])
print(s[:5])    #not specified start point means from the begining of the string
print(s[6:12])
print(s[6:])    #not specified end point means till the end of the string

x = {'foo': 'bar'}
y = {'baz': x}


