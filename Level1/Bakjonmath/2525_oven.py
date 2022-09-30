hr, mins = map(int, input().split())
time = int(input())

hr += time//60
mins += time % 60
if mins >= 60:
    hr += 1
    mins -= 60
if hr >= 24:
    hr -= 24
print('%d %d' % (hr, mins))
