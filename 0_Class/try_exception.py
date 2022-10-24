# Exception Try/

a = [1, 2, 3, 4, 5]

# a[5] index Error
b = "123@"
# ValueError: invalid literal for int() with base 10: '123@'
# c = int(b)

# method 1
try:
    b = "123@"
    c = int(b)
except:
    print("ValueError 발생")


# method 2
try:
    b = "123@"
    c = int(b)
except:
    print("ValueError occur")

# method 3

try:
    b = "123@"
    c = int(b)
except ValueError as v:
    print(v)


# method4
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    b = "123"
    c = int(b)
except ValueError as v:
    print(v)
else:
    print("No Error")

# method 5
# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    b = "123"
    c = int(b)
except ValueError as v:
    print(v)
finally:
    print("No Error")


# method6
try:
    f = open("sample.txt", "w")
    f.write("Heloo world")
except FileNotFoundError() as e:
    print(e)
finally:
    f.close()

# One try include several Error
try:
    a = [1, 2, 3]
    print(a[3]/0)
    print(a[3])
except IndexError:
    print("Wrong Index")
except ZeroDivisionError:
    print("Cannot divid by 0")


try:
    a = [1, 2, 3]
    print(a[3])
    print(10/0)
except (IndexError, ZeroDivisionError) as e:
    print(e)
