class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        for i in range(n):
            smallest = i

            for j in range(i + 1, n):
                if nums[j] < nums[smallest]:
                    smallest = j

            nums[i], nums[smallest] = nums[smallest], nums[i]

        result = []
        current = []

        def backtrack(index):
            temp = []

            for value in current:
                temp.append(value)

            result.append(temp)

            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)

        return result