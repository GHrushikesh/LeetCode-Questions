class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans = []
        for ch in s:
            if ch == y:
                ans.append(ch)
        for ch in s:
            if ch != x and ch!= y:
                ans.append(ch)
        for ch in s:
            if ch == x:
                ans.append(ch)
        return "".join(ans)