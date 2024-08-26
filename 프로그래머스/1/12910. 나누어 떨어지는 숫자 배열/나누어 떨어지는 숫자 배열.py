def solution(arr, divisor):
    answer = []
    cnt = 0
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0 :
            cnt += 1
            answer.append(arr[i])
            answer.sort()
    if cnt == 0 :
        return [-1]
    return answer