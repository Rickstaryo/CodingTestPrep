def solution(s1, s2):
    samecounter = 0
    for i in s1:
        for j in s2:
            if i == j:
                samecounter += 1
    return samecounter


# This is the Set you need to use built-in function.
# By using built in function, it's way easier to solve the problem.
#
def solution(s1, s2):
    return len(set(s1) & set(s2))
