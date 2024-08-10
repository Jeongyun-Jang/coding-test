# [PCCP 기출문제] 2번 / 석유 시추
# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    result = [0 for i in range(m)] # 획득한 총 석유량 
    visited = [[0] * m for _ in range(n)]
    
    def bfs(a, b):
        count = 0
        visited[a][b] = 1  # 방문 표시
        q = deque()
        q.append((a, b))
        min_y, max_y = b, b
        
        while q:
            x, y = q.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            count += 1
            for i in range(4):  # 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        
        for i in range(min_y, max_y + 1):  # max_y를 포함하도록 +1
            result[i] += count

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i, j)

    answer = max(result)
    return answer
