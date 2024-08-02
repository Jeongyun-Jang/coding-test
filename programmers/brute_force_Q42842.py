# 완전 탐색 > 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    w,h = 0,0
    divisors = []
    # brown + yellow = 총 격자
    # 총 가로,세로 경우의 수 확인 (약수) (가로, 세로) (1,12) (2,6) (3,4)
    # (가로-2)*(세로-2) == 노랑 수 => (1-2)*(12-2) != 노랑 수 (3-2)*(4-2) == 2 == 노랑수
    # 가로, 세로 어디가 더 긴지는 중요하지 않음
    
    totalSum = brown + yellow
    # 총 격자 약수
    for h in range(2, totalSum+1):
        if totalSum % h == 0:
            divisors.append(h)
    for h in divisors:
        w = totalSum // h
        # yellow 값과 같은지 확인
        if (w-2)*(h-2) == yellow:
            return [w,h]
    
    return answer