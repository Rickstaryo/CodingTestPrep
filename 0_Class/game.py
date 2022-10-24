# # 1. number guessing
import random

# print(" this is the game for guessing number")
# number = random.randint(1, 100)

# for _ in range(10):
#     guess = input(' Guess number from 0 to 100: ')
#     if number == int(guess):
#         print('Correct number {}'.format(number))
#         break
#     elif number > int(guess):
#         print('Wrong more bigger Number')
#     else:
#         print('Wrong more smaller Number')


# Make it on function

# def guess_Number(number):
#     cnt = 0
#     for _ in range(10):
#         guess = input(' Guess number from 0 to 100: ')

#         if number == int(guess):
#             print('Correct number {}'.format(number))
#             break
#         elif number > int(guess):
#             print('Wrong UP than '+guess)
#             cnt += 1
#         else:
#             print('Wrong Down then ' + guess)
#             cnt += 1
#         if(cnt > 9):
#             print("You fail the Game Correct was {}".format(number))
#             break


# random_number = random.randint(1, 100)
# guess_Number(random_number)


c = 10
print(c)


def add(a, b):
    c = a+b
    return c


print(c)
print(add(1, 2))
