# 더 맵게 heap
# Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
# 입출력 예
# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2

import heapq
def solution(scoville, K):
    # 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    spicy = heapq.heappop(scoville)
    answer = 0
    while spicy < K:
        try:
            # 가장 작은 두 개의 스코빌 지수를 꺼내어 새로운 스코빌 지수 생성
            new_spicy = spicy + heapq.heappop(scoville) * 2
            # 새로운 스코빌 지수를 힙에 추가
            heapq.heappush(scoville, new_spicy) 
            # 힙에서 가장 작은 요소를 꺼내어 spicy 변수 저장
            spicy = heapq.heappop(scoville)
            # 스코빌 지수를 섞은 횟수 증가
            answer += 1
        except:
            # 힙에서 요소를 꺼내는 도중 예외가 발생하면 -1 반환
            return -1
        

    return answer