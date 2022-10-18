a = set()
print(a)
print(type(a))

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a)
print(b)

print(a & b)

print(a-b)

a.add(6)
print(a)

a.remove(3)
print(a)

a.update([5, 6, 7, 8])
print(a)

# Changing data type

a = [1, 2, 3, 4, 5, 5, 5]
print(a)
b = list(set(a))
print(b)
