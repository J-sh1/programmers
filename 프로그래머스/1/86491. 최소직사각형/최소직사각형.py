def solution(sizes):
    max_width = 0
    max_height = 0
    
    for i in sizes:
        w, h = i
        if w < h:
            w, h = h, w
        max_width = max(max_width, w)
        max_height = max(max_height, h)
    
    return max_width * max_height