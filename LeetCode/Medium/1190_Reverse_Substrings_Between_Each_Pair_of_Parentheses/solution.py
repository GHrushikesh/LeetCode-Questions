class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""
        for ch in s:
            if ch == "(":
                stack.append(current)
                current = ""
            elif ch == ")":
                left = 0
                right = len(current) - 1
                chars = []
                for c in current:
                    chars.append(c)
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                reversed_string = ""
                for c in chars:
                    reversed_string += c
                previous = stack.pop()
                current = previous + reversed_string
            else:
                current += ch
        return current