class Solution:
    def fib(self, n: int) -> int:
        a1 = 0
        a2 = 1
        if n == 0:
            return a1
        if n == 1:
            return a2
        i = 2
        while i <= n:
            res = a1 + a2
            a1 = a2
            a2 = res
            i += 1
        return a2 % 1000000007


if __name__ == "__main__":
    s = Solution()
    print(s.fib(3))