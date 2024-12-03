tuple=(1,2,3,3,4,5,6,7,8)

print(tuple[0])

print(tuple[0:5])

print(tuple[5:])

print(tuple[::2])

print(tuple[::-1])

tuple=tuple[:3]+(9,)+tuple[3:]

print(tuple)