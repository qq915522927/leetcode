"""
类似于 将一个 string转换为 number

遍历每一位， 每多出一位 就在之前的结果上面乘以 进制数
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        cur = head;
        res = 0
        while cur is not None:
            res = res * 2 + cur.val
            cur = cur.next
        return res
