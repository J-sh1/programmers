def solution(cards1, cards2, goal):
    cnt1, cnt2 = 0, 0 

    for word in goal:
        if cnt1 < len(cards1) and cards1[cnt1] == word:
            cnt1 += 1
        elif cnt2 < len(cards2) and cards2[cnt2] == word:
            cnt2 += 1
        else:
            return "No"

    return "Yes"

# cards1[cnt1] == word cnt를 + 하면서 검사하는데 배열안에 값을 제거하는식으로도 가능