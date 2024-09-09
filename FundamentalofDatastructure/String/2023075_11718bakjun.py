while True:
    try:
        print(input())
    except EOFError:
        break


# First code
for _ in range(101):
    print(input())
