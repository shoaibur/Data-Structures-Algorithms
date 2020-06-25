def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i, j, k = m-1, n-1, len(nums1)-1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    for k, num in enumerate(nums2[:j+1]):
        nums1[k] = num
