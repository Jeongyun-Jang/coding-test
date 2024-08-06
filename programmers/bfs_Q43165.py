# dfs/bfs > 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    #계산 값을 담는 리스트
    leave = [0]    
    for number in numbers:
        # 임시 계산 값 저장
        tmp = []
        for leaf in leave:
            tmp.append(leaf + number)
            tmp.append(leaf - number)
        leave = tmp    
    return leave.count(target)