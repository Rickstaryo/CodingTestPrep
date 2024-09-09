# input s
s = str(input())
sr = ""
for i in s:
    sr += i+s
if(sr == s):
    print(1) else: print(0)
