# dfs/bfs > 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162


def dfs(n, computers, comNum, v):
    v[comNum] = True
    for connect in range(n):
        if connect != comNum and computers[comNum][connect] == 1: # 연결 되어 있으면
            if v[connect] == False:
                dfs(n, computers, connect, v)
            
def solution(n, computers): # 노드수, 연결정보
    answer = 0
    v = [False] * n
    
    for comNum in range(n): # 모든 노드(컴퓨터) 살펴보기
        if v[comNum] == False: # 연결되어 있지 않다면
            dfs(n, computers, comNum, v) # 연결되어 있는 것을 dfs로 확인
            answer += 1
    return answer
    