# Tuple
# list 는 [] tuple expressed by (), value cannot immutable
# Tuple is simpler than list and faster then list
# On the same time,tuple is safer than list
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
print(type(a), type(b))

# one Variable with various value then generate tuple
a = 1, 2, 3, 4
print(a)
# unpacking
a1, a2, a3, a4 = a
print(a1, a2, a3, a4)


# Indexing

a = 1, 2, 3, 4
print(a[0])
print(a[0:2])

b = 3, 4
print(a+b)
print(b*3)
# (3, 4, 3, 4, 3, 4)
