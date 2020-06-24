    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        out = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    a = sorted([nums[i], nums[j], nums[k]])
                    out.add(tuple(a))
                    j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return out
