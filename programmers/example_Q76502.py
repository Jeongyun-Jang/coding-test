# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0    
    openList = '{[('
    closeList = '}])'    
    dic = {'}':'{', ']':'[', ')':'('}
    for i in range(len(s)):
        res = s[i:] + s[:i]
        stack = []
        is_valid = True
        for char in res:      
            if char in openList:
                stack.append(char)
            elif char in closeList:
                if stack and stack[-1] == dic[char]: 
                    stack.pop()
                else:
                    is_valid = False
                    break
        if is_valid and not stack:
            answer += 1
    return answer
