
# https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/comments/

# use stack to reverse a linkedList

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next

        while stack:
            res.append(stack.pop().val)
        return res

