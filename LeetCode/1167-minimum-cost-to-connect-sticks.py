class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total = 0
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, cost)
            total += cost
        return total
