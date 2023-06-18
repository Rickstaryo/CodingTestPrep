case = int(input())
for c in range(case):
    numofa = int(input())
    A = list(set([int(x) for x in input().split()]))
    numofb = int(input())
    B = list(set([int(x) for x in input().split()]))
    numofc = int(input())
    C = list(set([int(x) for x in input().split()]))
    luckyNum = []

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(C)):
                temp = str(A[i] + B[j] + C[k])
                lucky = True
                for l in range(len(temp)):
                    if not (temp[l] == '5' or temp[l] == '8'):
                        lucky = False
                        break
                if lucky:
                    luckyNum.append(temp)
    luckyNum = set(luckyNum)
    print(len(luckyNum))
