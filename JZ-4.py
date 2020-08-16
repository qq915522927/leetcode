# // https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
class Solution:
    """
    关键点是利用 二维数组 从左到右，从上到下依次增大的特点
    每次选取又上角的点来和target元素作比较

    每次比较可排除一行，或一列


    """
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not matrix[0]:
            return False
        n = 0
        m = len(matrix[0]) - 1
        while m >= 0 and n < len(matrix):
            ele = matrix[n][m]
            if ele == target:
                return True
            if ele > target:
                m -= 1
            if ele < target:
                n += 1

        return False

