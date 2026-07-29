class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        for a in nums1:
            count[a] = 1
        result = []

        for a in nums2:
            if a in count:
                result.append(a)
                del count[a]
        return result