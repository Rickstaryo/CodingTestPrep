def solution(s):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"]
    for indx, num in enumerate(units):
        if num in s:
            s = s.replace(num, indx)
        ans = s
    return int(ans)
