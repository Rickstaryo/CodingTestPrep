def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    a = bin(a+b)
    return a.replace("0b", "")
