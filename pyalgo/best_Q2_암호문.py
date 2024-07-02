def solution(data):
    arr = ['r', 'e', 'v']
    result = 0
    i = 0
    while i < len(data) - 1:
        if data[i] in arr:
            # 다음 두 문자가 '10'인지 확인
            if i + 2 < len(data) and data[i + 1] == '1' and data[i + 2] == '0':
                result += 10
                i += 3  # '10'을 처리했으므로 두 칸 이동
            elif data[i + 1].isdigit():
                result += int(data[i + 1])
                i += 2  # 한 칸만 이동
            else:
                i += 1
        else:
            i += 1
    
    month = result // 10
    day = result % 10
    return str(month) + '월 ' + str(day) + '일'