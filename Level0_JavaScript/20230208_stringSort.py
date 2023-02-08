def solution(my_string):
    a = []
    for x in my_string:
        if x.isdigit():
            a.append(int(x))
    a.sort()
    return a


# Why the sort doesn't work 
# 1. I need to see the Sort and Sorted function 
    def solution(my_string):
    a = []
    for x in my_string:
        if x.isdigit():
            a.append(int(x))
    
    return sorted(a)