def solution(s):
    answer = ''
    b = []
    for i in range(0, len(s)):
        b.append(s[i])
    b.sort(reverse=True)
    for i in range(0, len(b)):
        answer += b[i]
    return answer