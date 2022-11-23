import requests
import random
import time
w = ['What doesnt kill you makes you stronger',
     'Stand a little taller',
     'Doesnt mean I am lonely when I am alone',
     'And do the things I want']

print("If you want to start press Enter")
input()
start = time.time()
end = time.time()
et = end - start

print("타자 시간 :", et, "초")

for str in w:
    user_input = input(str+"\n")
    correct = 0
    total_len = len(w[0])
    for i, c in enumerate(user_input):
        # print(i, c)
        if c == str[i]:
            correct += 1
    # Correctness
    c = correct / total * 100

    # wrongness
    e = (total_len-correct)/total_len*100

    # Velocity
    v = (correct/et) * 60

print(
    "Correctness: {:0.2f}, Wrongness:{:0.2f},Velocity{:0.2f}".format(c, e, v))


url = "http://www.naver.com"
print(url)
