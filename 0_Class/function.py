# Built-in Function

import math
print(type(int("100")))
print((int("100", 16)))  # 16
print((int("100", 8)))  # 8
print((int("100", 2)))  # 2

print(type(float("10.1")))
print(0.1+0.2)

print(math.isclose(0.1+0.2, 0.3))
# Determine whether two floating point numbers are close in value.

a = "jack, michele, queen"
print(a.split(','))


#  absolute
a = -1
print(abs(a))

# Sum

print(sum([1, 2, 3, 4, 5]))
# return True if bool(x) is True for all values x in the iterable.
# print(all[True, True])
print(all([0, 0]))
print(all([0, 1]))
# ASCII Code convert
print(chr(97))
print(ord('a'))

# 16,8 ,
print(bin(10))
print(oct(10))
print(hex(10))

# isinstance()
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
a = 10
print(isinstance(a, int))
print(isinstance(a, str))

# Round
a = 1/3
print(a)
print(round(a))
print(round(a, 3))


def is_prime(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False
    return True


a = is_prime(30)
print(a)


def restaurant(food, drink, dessert):
    return {'food': food, 'drink': drink, dessert: dessert}


order = restaurant('steak', 'cola', 'CarrotCake')
print(order)

second_order = restaurant(drink="soda", food="hamon", dessert="melon")
print(second_order)

# Default prameter


def restaurant2(food='pizza', drink='sozu', dessert='icecream'):
    return {'food': food, 'drink': drink, dessert: dessert}


print(restaurant2())
print(restaurant2('donkatu', 'beer'))


c = 10
print(c)


def add(a, b):
    c = a+b  # C is gloable Attribute that's why
    return c


print(add(1, 2))
print(c)


def save_winnrer(*args):  # Return with tuple
    print(args)


save_winnrer('john')
save_winnrer('john', 'flick')
save_winnrer('john', 'flck', 'bunga')


def save_winnrer2(**kwargs):  # Return with dictionary
    print(kwargs)


save_winnrer2(name1='gil', name2='gari')


def add(a, b):
    return a+b


def calc(func, a, b):
    print("Result {}".format(func(a, b)))


calc(add, 1, 5)
