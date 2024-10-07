def solution(cards1, cards2, goal):
    cnt1, cnt2 = 0, 0 

    for word in goal:
        if cnt1 < len(cards1) and cards1[cnt1] == word:  # cards1에서 단어를 사용할 수 있는지 확인
            cnt1 += 1
        elif cnt2 < len(cards2) and cards2[cnt2] == word:  # cards2에서 단어를 사용할 수 있는지 확인
            cnt2 += 1
        else:
            return "No"  # 둘 중 어느 카드 뭉치에서도 단어를 사용할 수 없다면 No 반환

    return "Yes"  # 모든 단어를 순서대로 사용할 수 있었다면 Yes 반환