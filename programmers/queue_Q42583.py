# 스택/큐 > 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    curWeight = 0
    
    while bridge:
        time += 1
        curWeight -= bridge.popleft()
        if truck_weights:
            if curWeight + truck_weights[0] <= weight:
                curWeight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time 
