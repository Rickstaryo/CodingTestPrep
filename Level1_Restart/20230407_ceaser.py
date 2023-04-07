def solution(s, n):
    #     1.일정한 순번이 있으니 리스트를 만든다

    s = list(s)
    for i in range(len(s)):
        #         2. 분기 시켜 준다
        if s[i].isupper():
            #         3. 아스키코드로 바꿔준다 더해준다
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)
