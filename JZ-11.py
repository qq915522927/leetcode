# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        if numbers[0] == numbers[-1]:
            # 如果是 一个 这样的  [1,1,2,3,0,1,1,1]
            # 无法判断中间的一个元素 是属于前半部分，或者后半部分，使用便利的方式
            min_n = numbers[0]
            for i in numbers:
                if i < min_n:
                    min_n = i
            return min_n
        if numbers[0] < numbers[-1]:
            # 顺序的数组
            return numbers[0]

        left = 0
        right = len(numbers) - 1

        # 二分查找
        while left != right - 1:
            mid = (left + right) // 2

            if numbers[mid] >= numbers[left]:
                left = mid

            if numbers[mid] <= numbers[right]:
                right = mid
        return numbers[right]

if __name__ == "__main__":
    s = Solution()
    print(s.minArray([3,4,5,1,2]))



