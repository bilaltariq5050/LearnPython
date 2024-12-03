# random_string = "I am Batman"  # 11 characters
# print(len(random_string),"Characters")

batman = "Bruce Wayne"
print(len(batman))
first = batman[0]  # Accessing the first character
print(first)
space = batman[5]  # Accessing the empty space in the string
print(space)
last = batman[len(batman) - 1]
# last=batman[10]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]

# batman = "Bruce Wayne"
# print(batman[-1])  # Corresponds to batman[10]
# print(batman[-5])  # Corresponds to batman[6]

# string = "I am Immutable"
# string[0] = '0' # Will give error