# 연습문제 > 미로 탈출

# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def is_valid_move(maze, visited, row, col):
    rows, cols = len(maze), len(maze[0])
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1 and not visited[row][col]

def bfs(start, end, maps):
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    que = deque()
    flag = False
    
    for i in range(n):
        for j in range(m):
            # 출발하고자 하는 지점이라면 시작점의 좌표를 기록
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                visited[i][j] = True
                flag = True; break 
                # 시작 지점은 한 개만 존재
        if flag: break
                
    # BFS
    while que:
        y, x, cost = que.popleft()
        
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0<= ny <n and 0<= nx <m and maps[ny][nx] != 'X':
                if not visited[ny][nx]: # 아직 방문하지 않은 통로라면
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1

def solution(maps):
    # S -> L -> E로 가기 위한 두 번의 BFS 실행
    path1 = bfs('S', 'L', maps) # 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
    return -1
