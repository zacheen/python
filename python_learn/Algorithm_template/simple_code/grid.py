def is_overlap(region1, region2):
    p0 = max(region1[0], region2[0])
    p1 = min(region1[1],region2[1])
    if p0 <= p1 :
        p2 = max(region1[2], region2[2])
        p3 = min(region1[3],region2[3])
        if p2 <= p3 :
            return [p0,p1,p2,p3]
    return None