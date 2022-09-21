
def solution(strings, n):
    strings.sort()
# sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
    return sorted(strings, key=lambda x: x[n])

#  Study for Ramda

# 해싱(hashing) 이란?
# 선형 탐색이나 이진 탐색은 모두 키를 저장된 키 값과 반복적으로 비교함으로써 탐색하고자 하는 항목에 접근한다. 이런 방법들은 최대 가능한 시간 복잡도가 O(logn)에 그친다. 이정도만 되어도 괜찮은 응용도 있지만, 어떤 응용에서는 더 빠른 탐색 알고리즘을 요구한다. 해싱은 키에 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근한다.


# 해시 테이블(hash table) : 이렇게 키에 대한 연산에 의해 직접 접근이 가능한 구조
# 해싱(Hashing) : 해시 테이블을 이용한 탐색
# lambda 매개변수: 리턴값
def lambdas(x):
    def power(x): return x * x
    def under_3(x): return x < 3

    list_input_a = [1, 2, 3, 4, 5]

    output_a = map(power, list_input_a)
    print("#map() 함수의 실행결과")
    print("map(power,list_input_a):", output_a)
    print("map(power, list_input_a):", list(output_a))
    print()
