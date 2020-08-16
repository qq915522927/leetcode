# https://leetcode.com/problems/magnetic-force-between-two-balls/
from timeit import default_timer as timer
# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#         position.sort()
#         min_backet = position[0]
#         max_backet = position[-1]

#         if m == 2:
#             return max_backet - min_backet

#         avg_unit = (max_backet - min_backet + 1) // (m -1)

#         ball_position = [position[0]]

#         left  = 0
#         right = len(position) - 1
#         last_ball_position = ball_position[0]
#         while len(ball_position) < m - 1:
#             target = self.find_closest(position, ball_position + avg_unit, left, right)
#             last_ball_position = target


#     def find_closest(self, position, value, left, right):
#         # 返回最接近的 下标

#         left = left
#         right = right

#         last_left = 0
#         last_right = 0
#         while left <= right:
#             if (left == right - 1):
#                 last_left = left
#                 last_right = right
#             mid = left + right // 2
#             if position[mid] == value:
#                 return mid
#             if position[mid] > value:
#                 right = mid - 1
#             if position[mid] < value:
#                 left = mid + 1
#         # 到这里， 说明没找到 exact的
#         # 那就取最接近的

#         if abs(position[last_left] - value) > abs(position[last_right]- value):
#             return last_right
#         else:
#             return last_left


class Solution2:
    """
    遍历所有组合
    """

    def maxDistance(self, position, m: int) -> int:
        self.cache = {}
        position.sort()
        return self._maxDistance(position, 0, len(position) - 1, m)

    def _maxDistance(self, position, left, right, m):
        if (left, right, m) in self.cache:
            return self.cache[(left, right, m)]
        if m == 3:
            i = 1
            max_v = 0
            while left + i < right:
                min_v = min(abs(position[left] - position[left+i]), abs(position[right] - position[left+i]))
                max_v = max(min_v, max_v)
                i += 1
            self.cache[(left, right, m)] = max_v
            return max_v
        if m == 2:
            return position[right] - position[left]

        maxDis = 0

        m = m -2
        i = right - (m-1) - left
        while i>=1:
        # i = 1
        # while left + i <= right - (m-1):
            j = right - (m-1) - left - i
            # j = 1
            # while left + i <= right - j - (m - 1):
            while j >= 1:
                if min(abs(position[left] - position[left + i]), abs(position[right] - position[right-j])) < maxDis:
                    j-=1
                    continue
                inner_max = self._maxDistance(position, left+i, right-j, m)

                minDis = min(*[abs(position[left] - position[left + i]), abs(position[right] - position[right-j]), inner_max])
                maxDis = max(minDis, maxDis)
                j -= 1
            i -= 1
        self.cache[(left, right, m+2)] = maxDis
        return maxDis


class Solution:
    """
    二分法
    """

    def maxDistance(self, position, m: int) -> int:

        position.sort()
        pre = None
        min_possible = 0
        for i in position:
            if pre is None:
                pre = i
                continue
            min_possible =min(i - pre, min_possible)
        max_possible = (position[-1] - position[0]) // (m - 1)

        while min_possible < max_possible - 1:
            mid_possible = (max_possible + min_possible) // 2
            if self.check_is_valid_min_length(position ,mid_possible, m):
                min_possible = mid_possible
            else:
                max_possible = mid_possible - 1

        if self.check_is_valid_min_length( position,max_possible, m):
            return max_possible
        else:
            return min_possible

    def check_is_valid_min_length(self, position, length, m):
        pre = None
        count = 0
        for i in position:
            if pre is None:
                count += 1
                pre = i
            if i - pre >= length:
                count += 1
                pre = i
            if count >= m:
                return True
        return False




if __name__ == "__main__":
    s = Solution()
    assert s.maxDistance([1,2,3,4], 2) == 3

    assert s.maxDistance([1,2,3,4], 3) == 1
    print( s.maxDistance([1,12, 20,40], 4) )

    # print(s.maxDistance([87,56,69,63,99,81,19,28,57,98,82,43,60,88,58,16,4,26,27,40,54,38,85,72,52,65,32,83,22,49,93,75,20,51,55], 20))
#     s1 = timer()
#     print(s.maxDistance([437329569,717804524,638409502,554642488,827554090,376763411,208461057,647335860,792881513,376325215,244438751,63038220,275095695,951101762,515490769,816284518,326035444,42526858,846803083,397151283,67069021,524200306,568155148,665657578,931035400,186843310,618970659,652299531,554557452,112541805,800737269,884817130,771753228,964038076,19774497,232518720,831955359,569155096,123309193,425913720,293892389,213100339,908222772,214351553,596185776,727144451,533634767,100662976,798951612,599775676,829455131,683638291,888730038,283127096,222713021,225880362,346153544,292145850,501895774,636213697,165211119,362227289,568939593,252546501,273642875,28999821,228602989,476164796,546940477,919877023,933250237,488938044,988759640,633065848,602382724,538917729,537599262,972696921,274151209,411615085,930637961,567813531,191109830,28396600,816294504,279597223,694400390,188504114,236769193,487199448],
# 25))
#     s2 = timer()
#     print(s2 - s1)

