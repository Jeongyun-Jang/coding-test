# 코딩테스트 > 예상 대진표
# https://school.programmers.co.kr/learn/courses/30/lessons/12985?language=python3

def solution(n,a,b):
    answer = 0
    is_valid = True
    while is_valid:
        answer += 1
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        if a == b:
            is_valid = False
            break
    return answer