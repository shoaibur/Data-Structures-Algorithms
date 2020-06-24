    def myAtoi(self, str: str) -> int:
        str = str.split()
        if len(str) < 1: return 0
        str = str[0]
        if str[0] not in '-+0123456789':
            return 0
        neg = False
        if str[0] == '-':
            neg = True
            str = '0' + str[1:]
        if str[0] == '+':
            neg = False
            str = '0' + str[1:]
        nums = []
        for char in str:
            if char not in '0123456789':
                break
            nums.append(char)
        nums = int(''.join(nums))
        if neg: nums = -nums
        if nums > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if nums < -2 ** 31:
            return -2 ** 31
        return nums
