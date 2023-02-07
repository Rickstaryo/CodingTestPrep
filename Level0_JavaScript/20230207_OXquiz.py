

def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)


def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]
