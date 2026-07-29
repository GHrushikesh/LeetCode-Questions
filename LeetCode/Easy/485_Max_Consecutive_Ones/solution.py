class Solution(object):
    def findMaxConsecutiveOnes(self, nums):

        current = 0
        best = 0

        for num in nums:

            if num == 1:
                current = current + 1

                if current > best:
                    best = current

            else:
                current = 0

        return best