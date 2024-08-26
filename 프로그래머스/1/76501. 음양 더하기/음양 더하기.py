def solution(absolutes, signs):
    answer = 0
    res = 0
    for i in range(0, len(signs)) :
        if signs[i] == False :
            res -= absolutes[i]
        else :
            res += absolutes[i]
        
    return res