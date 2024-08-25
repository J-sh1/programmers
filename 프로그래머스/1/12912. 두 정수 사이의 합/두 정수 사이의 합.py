def solution(a, b):
    res = 0
    if a == b :
        return a
    elif a <  b :
        for i in range (a , b + 1) :
            res += i
        return res
    else :
        for i in range (b , a + 1) :
            res += i
        return res
    
