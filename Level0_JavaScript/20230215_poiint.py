def solution(dot):
    if dot[0]>0 and dot[1]>0:
        return 1
    elif dot[0]>0 and dot[1]<0:
        return 4
    elif dot[0]<0 and dot[1]>0:
        return 2
    else:
        return 3
def solution(dot):
    x,y = dot
    if x*y>0:
        return 1 if x>0 else 3
    else:
        return 4 if x>0 else 2
