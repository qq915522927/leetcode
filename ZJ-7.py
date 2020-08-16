# https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归实现
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.get_tree(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def get_tree(self, preorder, inorder, pl, pr, il, ir):
        if pl > pr:
            return None
        root = preorder[pl]
        root_node = TreeNode(root)
        root_index = self.find(root, inorder, il, ir)


        num_left = root_index - il
        num_right = ir - root_index
        root_node.left = self.get_tree(preorder, inorder, pl + 1, pl + num_left, il, root_index - 1)
        root_node.right = self.get_tree(preorder, inorder, pl + num_left + 1, pr, root_index + 1, ir)
        return root_node

    def find(self, v, vals, l, r):
        while l <= r:
            if v == vals[l]:
                return l
            l += 1

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder:
            return None

        indexs = {}
        # 利用dict 存储 各个值得 index
        for i, v in enumerate(inorder):
            indexs[v] = i


        # 只要知道  pl, pr, il, ir 就能求出root 和 left, right
        root = preorder[0]
        root_node = TreeNode(root)
        root_node.pl, root_node.pr, root_node.il, root_node.ir = 0, len(preorder) - 1, 0, len(inorder) - 1

        stack = []
        stack.append(root_node)

        while stack:
            node = stack.pop()
            il, ir, pl, pr = node.il, node.ir, node.pl, node.pr
            root_index = indexs[node.val]
            left_num = root_index - il
            right_num = ir - root_index

            if left_num:
                new_pl1 = pl + 1
                new_pr1 = pl + left_num
                left_node = TreeNode(preorder[new_pl1])
                # 保存下一次迭代的 pl, pr, il, ir
                left_node.pl = new_pl1
                left_node.pr = new_pr1
                left_node.il = il
                left_node.ir = root_index - 1

                node.left = left_node
                stack.append(left_node)

            if right_num:
                new_pl2 = pl + left_num + 1
                new_pr2 = pr
                right_node = TreeNode(preorder[new_pl2])
                right_node.pl = new_pl2
                right_node.pr = new_pl2
                right_node.il = root_index + 1
                right_node.ir = ir

                node.right = right_node
                stack.append(right_node)
        return root_node



    # 如果用find, 时间复杂度 变为 O2, 不用它
    def find(self, v, vals, l, r):
        while l <= r:
            if v == vals[l]:
                return l
            l += 1