class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        a1 = 1
        a2 = 1

        i = 2
        while i <= n:
            a1, a2 = a2, a1 + a2
            i += 1
        return a2 % 1000000007


if __name__ == "__main__":
    s = Solution()
    print(s.numWays(6))
