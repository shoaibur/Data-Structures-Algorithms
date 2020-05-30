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
    i, j = -1, -1
    for k, num in enumerate(nums):
        if num == 1 and i == -1:
            i = k
        elif num == 1 and k == -1:
            j = k
        elif num == 1:
            i, j = j, k
        dis = j - i
        if dis > max_dis:
            max_dis = dis
            index = (i + j) // 2
    return index





class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats: return
        if all(seats): return
        i, j = -1, -1
        max_dis = 0
        for k, num in enumerate(seats):
            if num == 1 and i == -1:
                i = k
                if nums[0] == 0:
                    max_dis = i
                    index = 0
            elif num == 1 and j == -1:
                j = k
            elif num == 1:
                i, j = j, k
            
                dis = j - i
                if dis > max_dis:
                    max_dis = dis
                    index = (i + j) // 2
            
        return index
