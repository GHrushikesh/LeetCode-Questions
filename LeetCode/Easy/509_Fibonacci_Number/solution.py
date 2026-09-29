class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = self.fib(n - 1)
        second = self.fib(n - 2)
        answer = first + second
        return answer