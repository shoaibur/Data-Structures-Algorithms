def kth_largest(nums, k):
    if len(nums) < k: return None
    heap = heapify(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heap[0] = nums[i]
            heap = heapify(heap)
    return heap[0]
  
def heapify(heap):
    n = len(heap)
    if n <= 1: return heap
    for i in range(n-1, -1, -1):
        parent_index = i // 2
        if heap[parent_index] > heap[i]:
            heap[parent_index], heap[i] = heap[i], heap[parent_index]
    return heap
