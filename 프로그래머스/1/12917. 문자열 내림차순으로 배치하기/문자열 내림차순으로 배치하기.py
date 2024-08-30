def solution(s):
    answer = ''
    b = []
    for i in range(0, len(s)):
        b.append(s[i])
    b.sort(reverse=True)
    for i in range(0, len(b)):
        answer += b[i]
    return answer

# 다른사람 코드
# ''.join(sorted(s, reverse=True))
# 흠... 굳이 for문을 안돌려도 될듯? sorted