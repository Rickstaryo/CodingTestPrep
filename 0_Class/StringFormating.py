old = 30
a = "I am %d years old" % old
print(a)
h = 185.9
# %s: String
# %c : one character
# $d : interger
# %

a = "I am %d years old and height is %f Cm" % (old, h)
print(a)

a = "I am {} years old and height is {} Cm".format(old, h)
print(a)

# if you put in order you could choose the order
a = "number {}, {}, {}".format(1, 2, 3)
print(a)
# Reversing the order
a = "number {2}, {1}, {0}".format(1, 2, 3)
print(a)

name = "Max"
country = "America"
age = 30

print(f"I am {name} from {country}, I am {age} years old ")


# %number controll the space and blank
number = "%10.4f" % 3.131592
print(number)
