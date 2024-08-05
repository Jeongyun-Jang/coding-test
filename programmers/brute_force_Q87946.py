# 완전 탐색 > 피로도, DFS 풀이
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer = 0

def dfs(k, cnt, dungeons, check):
    global answer
    answer = max(answer,cnt)
    totalEnergy = k
    for i in range(len(dungeons)):
        # 방문 전이고 최소 피로도가 현재 남아있는 피로도 보다 작을 때
        if check[i] == 0 and k >= dungeons[i][0]:
            check[i] = 1
            totalEnergy = k-dungeons[i][1]
            dfs(totalEnergy, cnt+1, dungeons, check)
            check[i] = 0
            
def solution(k, dungeons):
    global answer
    # 방문 여부 체크 리스트
    check = [0] * len(dungeons)
    dfs(k, 0, dungeons, check)
    return answer