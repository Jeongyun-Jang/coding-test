# [' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - ']	'Jun'
#
# +는 1로, -는 0으로 변경되어 ' + - - + - + - '는 1001010이 됩니다.
# 이 숫자는 10진수로 바꾸었을 때 74로 아스키 코드표로 보면 대문자 J가 됩니다.
# 이와 같은 원리로 나머지 2개를 문자로 바꿔 조합하면 'Jun'이 됩니다.
# 
# https://pyalgo.co.kr/?page=1#

def solution(data):
    res = []
    result = ''
    for item in data:
        item = item.replace(' ', '')
        item = item.replace('+', '1')
        item = item.replace('-', '0')
        res.append(chr(int(item, 2)))
    for i in res:
        result += i
    return result
