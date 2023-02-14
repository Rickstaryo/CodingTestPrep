def solution(age):
    alien=["a","b","c","d","e","f","g","h","i","j"]
    answer = ''
    for i in str(age):
        answer+=alien[int(i)]
    return answer