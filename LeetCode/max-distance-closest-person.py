def max_distance_closest_person(seats):
    loc = [i for i,seat in enumerate(seats) if seat == 1]
    max_dis = 0

    if seats[0] == 0 and seats[-1] == 0:
        left_dis = loc[0]
        right_dis = len(seats) - 1 - loc[-1]
        max_dis = max(left_dis, right_dis)
    elif seats[0] == 0:
        max_dis = loc[0]
    elif seats[-1] == 0:
        max_dis = len(seats) - 1 - loc[-1]

    if len(loc) > 1:
        for i in range(len(loc)-1):
            dis = (loc[i+1] - loc[i]) // 2
            max_dis = max(max_dis, dis)
    return max_dis


def max_distance_closest_person(nums):
    if sum(nums) == 1:
            person = [i for i, num in enumerate(nums) if num == 1][0]
            return max(person-0, len(nums) - 1 - person)
    
    i, j = None, None
    max_dis = 0
    dis = 0
    for k, num in enumerate(nums):
        if num == 1 and i is None:
            i = k
            if i != 0:
                dis = i
        elif num == 1 and j is None:
            j = k
            dis = (j - i) // 2
        elif num == 1:
            i, j = j, k
            dis = (j - i) // 2
        elif k == len(nums) - 1 and j != k:
            dis = k - j
        max_dis = max(max_dis, dis)
    return max_dis
