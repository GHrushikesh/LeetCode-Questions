class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:

        prefix = {0: 1}

        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix:
                ans += prefix[needed]

            if current_sum in prefix:
                prefix[current_sum] += 1
            else:
                prefix[current_sum] = 1

        return ans