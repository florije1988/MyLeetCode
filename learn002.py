#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'florije'

# Recover Binary Search Tree
'''
一棵二叉搜索树中两个节点错误，修正这棵树。
正确二叉树中序遍历应该是递增，而交换了两个节点后会导致有一处或者两处某节点值小于前一个节点，记录，最后交换即可。
'''

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.pre = None
        self.n1 = self.n2 = None
        self.dfs(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre and root.val < self.pre.val:
            if not self.n1:
                self.n1, self.n2 = self.pre, root
            else:
                self.n2 = root
        self.pre = root
        self.dfs(root.right)


if __name__ == '__main__':
    pass