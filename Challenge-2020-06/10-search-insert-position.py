def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return None
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        if target < nums[mid]:
            return mid
        return low
