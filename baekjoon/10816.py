#숫자 카드 2 https://www.acmicpc.net/problem/10816

input_value1 = int(input()) 
N = list(map(int, input().split()))

input_value2 = int(input())
M = list(map(int, input().split()))
result = []

N = sorted(N)

for m in M:
    left, right = 0, len(N) - 1
    count = 0 
    
    while left <= right:
        mid = (left + right) // 2 
        if N[mid] == m:
            count = 1
            left_temp = mid - 1
            # 왼쪽에 중복된 m의 개수 카운트
            while left_temp >= 0 and N[left_temp] == m:
                count += 1
                left_temp -= 1
            right_temp = mid + 1
            # 오른쪽에 중복된 m의 개수 카운트
            while right_temp < len(N) and N[right_temp] == m:
                count += 1
                right_temp += 1
            break
        elif N[mid] < m:
            left = mid + 1
        else:
            right = mid - 1
    
    result.append(count)

print(' '.join(map(str, result)))
