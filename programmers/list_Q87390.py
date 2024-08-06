# n^2 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    mtrx = []
    for i in range(left, right+1):
        # 해당 인덱스 값
        row = i // n
        col = i % n
        mtrx.append(max(row, col)+1)
            
    return mtrx