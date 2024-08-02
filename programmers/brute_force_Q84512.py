# 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    res = 0
    num_arr = []

    
    # 사전 자리값
    # 1 자리: 5^4 + 5^3 + 5^2 + 5^1 + 5^0 = 781
    # 2 자리: 5^3 + 5^2 + 5^1 + 5^0 = 156
    # 3 자리: 5^2 + 5^1 + 5^0 = 31
    # 4 자리: 5^1 + 5^0 = 6
    # 5 자리: 5^0 = 1
        
    for i in range(4,-1,-1):
        num_arr.append((5**(i+1)-1)//4)

    word_set = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    answer = len(word)
    
    for i in range(len(word)):
        answer += num_arr[i] * word_set[word[i]]       

    return answer