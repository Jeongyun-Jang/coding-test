# 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

# 내가 푼 문제  => 시간 초과
def solution(k, d):
    answer = 0    
    
    for i in range(0,d+1,k):
        for j in range(0,d+1,k):
            print(i,j)
            if (i**2) + (j**2) <= d**2:
                answer += 1
        
    return answer


# 최적화 된 코드
import math

def solution(k, d):
    answer = 0
    
    for i in range(0, d+1, k):
        max_j = math.isqrt(d**2 - i**2)
        answer += (max_j // k) + 1
        
    return answer