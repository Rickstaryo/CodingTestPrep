str = input()  # 문자열 S 입력받기
result = []  # 접미사를 담을 배열 생성
for i in range(len(str)):
    result.append(str[i:])  # 접미사 result에 추가
for r in sorted(result):  # 정렬한 접미사 가져오기
    print(r)  # 출력
