def max_distance_closest_person(nums):
    loc = []
    for i, num in enumerate(nums):
        if num == 1:
            loc.append(i)
    max_dis = 0
    max_index = -1
    for i in range(len(loc)-1):
        dis = loc[i+1] - loc[i]
        if dis > max_dis:
            max_dis = dis
            max_index = ( loc[i] + loc[i+1] ) // 2
    return max_index
