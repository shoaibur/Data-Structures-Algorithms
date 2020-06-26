def findKthLargest(nums):
    if not nums or k < 1 or len(nums) < k: return -1
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            #heap[0] = num
            #heapq.heapify(heap)
            heapq.heapreplace(heap, num)
    return heap[0]
