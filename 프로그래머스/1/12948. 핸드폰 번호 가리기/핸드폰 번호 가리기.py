def solution(phone_number):
    answer = ''
    a = (len(phone_number)-4)
    b = '*'
    return f'{b * a}{phone_number[-4:]}'