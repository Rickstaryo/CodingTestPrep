def solution(age):
    alien=["a","b","c","d","e","f","g","h","i","j"]
    answer = ''
    for i in str(age):
        answer+=alien[int(i)]
    return answer

def solution(age):
    #alien=["a","b","c","d","e","f","g","h","i","j"]
    #answer = ''
    #for i in str(age):
    #   answer+=alien[int(i)]  
    return"".join([chr(int(i)+97) for i in str(age)])