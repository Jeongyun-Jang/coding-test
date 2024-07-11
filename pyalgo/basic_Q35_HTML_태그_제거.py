import re
def solution(data):
    pattern = r"<[^>]+>" #<로 시작하고 그 다음에 >가 아닌 문자들이 하나 이상 있으며 >로 끝나는 문자열
    return re.sub(pattern, "", data) #pattern을 제외하여 return

print(2//3)