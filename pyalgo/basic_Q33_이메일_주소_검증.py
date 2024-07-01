# user@example.com	True
#
# local-part@domain 형식을 따릅니다. 여기서 local-part는 대소문자, 숫자, 특정 특수 문자(., _, +)를 포함할 수 있고, domain은 대소문자, 숫자, 하이픈(-)과 점(.)을 포함할 수 있습니다.
# domain의 마지막 부분은 점(.)으로 구분된 두 글자 이상의 알파벳 문자열이어야 합니다.
#
# https://100.pyalgo.co.kr/?page=33#
import re
def solution(data):
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not pattern.match(data):
        return False
    last, next = data.split('@')
    if next.rfind('.') == -1 or len(next[next.rfind('.'):]) < 2:
        return False
    return True