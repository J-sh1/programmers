def solution(s):
    answer = True
    cnt = ''.join(s)
    print(len(cnt))
    if len(cnt) == 4 or len(cnt) == 6 :
        try :
            int(s)
            return True
        except :
            return False
    else :
        return False
    
