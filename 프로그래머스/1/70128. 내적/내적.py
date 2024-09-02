def solution(a, b):
    cnt = 0
    for i in range(0, len(a)):
        cnt += (a[i] * b[i])
    return cnt