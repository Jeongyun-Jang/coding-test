# 완전 탐색 > 전력망을 둘로 나누기 DFS 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/86971 

def dfs(cur, wires, ch):
    global tmp
    
    # 현재 노드 기준으로 DFS 수행
    for i in range(len(ch)-1):
        # 아직 방문 x
        if ch[i] == 0:
            for j in range(2):
                # 연결된 간선이면
                if wires[i][j] == cur:
                    # 방문 처리
                    ch[i] = 1
                    # 연결된 노드 수 증가
                    tmp += 1
                    # 연결된 노드로 DFS 재귀 호출
                    dfs(wires[i][(j+1)%2], wires, ch)

def solution(n, wires):
    # 방문 상태 저장 리스트
    ch = [0] * n
    res = []
    global tmp
    
    # 각 간선 제거시 두 트리의 노드 개수
    for i in range(n-1):
        tmp = 1
        # 방문 표시
        ch[i] = 1 
        a, b = wires[i][0], wires[i][1]
        
        # 노드 a를 시작으로 노드 개수 세기
        dfs(a, wires, ch)
        # 방문 상태 초기화
        ch[i] = 0
        # 두 트리의 노드 개수 차이를 결과 리스트에 추가
        res.append(abs(2 * tmp - n))
    
    # 노드 개수 차이 최소값 반환
    return min(res)
