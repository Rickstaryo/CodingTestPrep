money = 1250
arr = [500, 100, 50, 10]
for i in arr:
    coin += money//i
    money = money % i
print(coin)
