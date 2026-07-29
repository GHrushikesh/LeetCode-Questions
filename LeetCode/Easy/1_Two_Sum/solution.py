from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # maps value -> index
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        # Problem guarantees a solution; raise for safety
        raise ValueError("No two sum solution")