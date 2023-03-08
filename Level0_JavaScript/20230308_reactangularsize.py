def solution(dots):
    Xdots = [dot[0] for dot in dots]
    Ydots = [dot[1] for dot in dots]
    return (max(Xdots)-min(Xdots))*(max(Ydots)-min(Ydots))
