class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        prevMap =  {} # val :index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            return