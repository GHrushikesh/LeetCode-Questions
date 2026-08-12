class Solution:
    def reverseWords(self, s: str) -> str:
        chars = []
        for ch in s:
            chars.append(ch)
        left = 0
        right = len(chars) - 1
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        ans = ""
        i = 0
        while i < len(chars):
            while i < len(chars) and chars[i] == ' ':
                i += 1
            if i >= len(chars):
                break
            start = i
            while i < len(chars) and chars[i] != ' ':
                i += 1
            end = i - 1
            left = start
            right = end
            while left < right:
                chars[left], chars[right] = chars[right] , chars[left]
                left += 1
                right -= 1
            if len(ans)> 0:
                ans += " "
            j = start
            while j <= end:
                ans += chars[j]
                j += 1 
        return ans