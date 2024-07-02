def solution(data):
    # 숫자인지 확인
    new_data = data.replace(" ","")
    str_result = []
    tuple_result = []
    
    while i < len(new_data):
        if new_data[i].isdigit():
            j = i
            while j < len(new_data) and new_data[j] not in [',', '.']:
                j += 1
            str_result.append(new_data[i:j])
            i = j
        else:
            i += 1
    
    for item in str_result:
        tuple_result.append(tuple(int(item) for item in item.split('-')))                  
    
    return tuple_result