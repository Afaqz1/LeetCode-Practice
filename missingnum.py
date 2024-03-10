class Solutions:
    def missingnum(self, nums: list[int])-> int:
        res = 0
        for i in range(len(nums)):
            res += (i-nums[i])

        return res 