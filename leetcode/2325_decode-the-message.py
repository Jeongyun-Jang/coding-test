class Solution(object):
  def decodeMessage(self, key, message):
    """
    :type key: str
    :type message: str
    :rtype: str
    """
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # key와 alphabet을 매핑할 딕셔너리
    decode = {}
    index = 0
    res = []
    
    for char in key:
      # 공백이 아니고, decode에 없는 문자라면 매핑
      if char != ' ' and char not in decode:
        decode[char] = alphabet[index]
        index += 1
    
    
    # message 해독
    for char in message:
        if char == ' ':
          res.append(' ')
        else:
          # 매핑된 문자 추가
          res.append(decode.get(char, char))
    
    return ''.join(res)
