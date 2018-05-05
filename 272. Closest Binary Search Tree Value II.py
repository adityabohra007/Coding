"""
用heap做，储存 绝对值的负值，因为heap只能弹出最小值
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import heapq


class Solution(object):
    def closestKValues(self, root, target, k):
        self.heap = []
        self.dfs(root, target, k)
        result = []
        while len(self.heap) > 0:
            result.append(heapq.heappop(self.heap)[1])
        return result

    def dfs(self, root, target, k):
        if root is None:
            return
        heapq.heappush(self.heap, (-abs(root.val - target), root.val))
        if len(self.heap) > k:
            heapq.heappop(self.heap)
        self.dfs(root.left, target, k)
        self.dfs(root.right, target, k)

"""
用中序遍历得到从小到大的数组
用二分法定位离target最近的start和end
分别向两边遍历
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        result = []
        if root is None:
            return result
        self.list = []
        self.inOrder(root)
        result = self.findK(self.list, target, k)
        return result

    def findK(self, list, target, k):
        start = 0
        end = len(list) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if list[mid] < target:
                start = mid
            else:
                end = mid
        output = []
        while len(output) < k:
            leftDiff = abs(target - list[start]) if start >= 0 else None
            rightDiff = abs(target - list[end]) if end < len(list) else None

            if leftDiff != None and rightDiff != None:
                if rightDiff < leftDiff:
                    output.append(list[end])
                    end += 1
                else:
                    output.append(list[start])
                    start -= 1
            elif leftDiff != None:
                output.append(list[start])
                start -= 1
            elif rightDiff != None:
                output.append(list[end])
                end += 1
        return output

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        self.list.append(root.val)
        self.inOrder(root.right)