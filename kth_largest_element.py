class Solution:
    def first_and_last(self, arr: list[int], target:list[int]) ->list[int]:
        for i in range(len(arr)):
            if arr[i] == target:
                start = i
                while i+1 < len(arr) and arr[i+1] == target:
                    i += 1
                return [start, i]
        return [-1, -1]