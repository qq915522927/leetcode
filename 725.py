# https://leetcode.com/problems/split-linked-list-in-parts/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        cur = root
        # 先求 list的长度
        while cur is not None:
            n += 1
            cur = cur.next

        # 计算 每个part平均装多少元素
        if n >= k:
            size = n // k
            more = n % k
        else:
            size = 1
            more = 0

        res = []

        cur = root
        i = 0
        cur_size = 0
        head = None
        last = None
        while cur is not None:
            if cur_size == 0:
                head = cur
            cur_size += 1;
            if cur_size == size:
                if more > 0:
                    more -= 1
                else:
                    i += 1
                    cur_size = 0
                    res.append(head)
                    last = cur
            elif cur_size > size:
                i += 1
                cur_size = 0
                res.append(head)
                last = cur
            cur = cur.next
            if last:
                last.next = None

        if i < k:
           while i < k:
               res.append(None)
               i += 1
        return res
