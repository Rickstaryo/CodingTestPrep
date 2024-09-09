#input
a,b,c=map(int,input())
# 1 to 100
arr=[0]*100
for _ in range(3):
    m,n=map(int,input())
    for i in range(m,n+1):
        arr[i]+=1

for i in arr:
    if i==1:
        sum+=i*a
    elif i==2:
        sum+=i*b
    else:
        sum+=i*c
print(sum)
