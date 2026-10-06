class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []
        used = [False] * len(nums)
        def backtrack():
            if len(nums) == len(current):
                temp = []
                for value in current:
                    temp.append(value)
                result.append(temp)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False
        backtrack()
        return result