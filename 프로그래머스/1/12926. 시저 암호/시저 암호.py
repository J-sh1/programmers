def solution(a, n):
    answer = ''
    for i in range(0, len(a)):
        if a[i].isalpha():  
            if a[i].islower():  
                answer += chr((ord(a[i]) - ord('a') + n) % 26 + ord('a'))
            elif a[i].isupper(): 
                answer += chr((ord(a[i]) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += a[i]  
    return answer