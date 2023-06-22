import sys
input=sys.stdin.readline


while True:
    N,M=map(int,input().split())

    if N==0 and M==0:
        exit(0)

    N_list=[] ; M_list=[]

    for i in range(N):
        N_list.append(int(input()))

    for i in range(M):
        M_list.append(int(input()))

    index_N=0 ; index_M=0 ; total=0

    while index_N<N and index_M<M:

        if N_list[index_N]==M_list[index_M]:
            total+=1
            index_N+=1 ; index_M+=1

        elif N_list[index_N]>M_list[index_M]:
            index_M+=1
        else:
            index_N+=1

    print(total) 