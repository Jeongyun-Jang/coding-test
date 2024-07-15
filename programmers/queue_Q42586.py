# 스택/큐 기능 개발
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
# 입출력 예
# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque

def solution(progresses, speeds):
    days_remaining = deque()
    days = 0
    remaining_work = 0
    count = 0
    
    for i in range(len(progresses)):
        remaining_work = 100 - progresses[i]
        if remaining_work % speeds[i] == 0:
            days = remaining_work // speeds[i]
        else:
            days = (remaining_work // speeds[i]) + 1
        days_remaining.append(days)
        
    answer = []
    
    while days_remaining:
        current = days_remaining.popleft()
        count = 1
        
        while days_remaining and days_remaining[0] <= current:
            days_remaining.popleft()
            count += 1
        answer.append(count)
        
        
    return answer