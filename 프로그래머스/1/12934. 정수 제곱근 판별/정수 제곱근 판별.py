def solution(n):
    x = 1
    while x * x <= n:
        if x * x == n:
            return (x + 1) * (x + 1)
        x += 1
    return -1
