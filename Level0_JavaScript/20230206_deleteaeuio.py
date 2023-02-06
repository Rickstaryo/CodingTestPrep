
def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string
