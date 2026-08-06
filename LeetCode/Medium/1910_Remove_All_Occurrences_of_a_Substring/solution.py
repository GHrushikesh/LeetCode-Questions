class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part):
                match = True
                for i in range(len(part)):
                    if stack[len(stack) - len(part) + i] != part[i]:
                        match = False
                        break
                if match:
                    for i in range(len(part)):
                        stack.pop()
        ans = ""
        for ch in stack:
            ans += ch
        return ans