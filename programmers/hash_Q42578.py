#https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 제한사항
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
# 코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
# 같은 이름을 가진 의상은 존재하지 않습니다.
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

# 입출력 예
# clothes	return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]] 3

def solution(clothes):
    answer = 1
    dic = {}
    for clothe in clothes:
        if clothe[1] not in dic:
            dic[clothe[1]] = 0
        dic[clothe[1]] += 1
    for k in dic.keys():
        answer *= dic[k] + 1
    return answer - 1