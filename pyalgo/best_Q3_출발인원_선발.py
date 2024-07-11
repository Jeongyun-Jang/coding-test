def solution(data):
    # 데이터 길이가 3명 미만일 경우 빈 리스트 반환
    if len(data) < 3:
        return []

    total_man = len(data) // 3
    if total_man < 1:
        return []

    res = {}
    result = []

    # 각 항목에 대해 평균을 계산하여 딕셔너리에 저장
    for item in data:
        if len(item) > 1:  # 이름을 제외한 데이터가 있을 때만 평균을 계산
            avg = sum(item[1:]) / (len(item) - 1)
        else:
            avg = 0
        res[item[0]] = avg

    # 평균이 높은 사람들을 찾기
    while total_man > 0 and res:
        selected_avg = set()
        max_person = max(res, key=res.get)
        if max_person in selected_avg:
            return []
        else:
            result.append(max_person)
            del res[max_person]
            selected_avg.add(max_person)
            total_man -= 1
    
    result.reverse()
    return result