def solution(price, money, count):
    pay = 0
    for i in range(1, count+1):
        pay += (i*price)
    if(pay > money):
        return pay-money
    else:
        return 0


def Bettersolution(price, money, count):
    #     등차수열 의 합공식 사용
    #    n(a+l)//2
    return max(0, count*(price + (price*count))//2-money)
