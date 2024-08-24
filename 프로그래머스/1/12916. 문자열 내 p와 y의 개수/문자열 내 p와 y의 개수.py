def solution(s):
    answer = True
    p = 0
    y = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    s = ''.join(s.lower())
    for i in range(0, len(s)):
        if s[i] == 'p' :
            p += 1
        elif s[i] == 'y' :
            y += 1
    
    if p == y :
        return True
    else : 
        return False