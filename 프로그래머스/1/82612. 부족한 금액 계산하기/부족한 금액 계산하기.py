def solution(price, money, count):
    a = 0
    b = 0
    for i in range(1, count + 1) :
        a = price * i
        b += a
    if b - money < 0 :
        return 0
    return b - money