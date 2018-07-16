# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '[]'

        from collections import defaultdict, deque
        q = deque([root])
        result = '['
        while q:
            rowLen = len(q)
            for i in xrange(rowLen):
                node = q.popleft()
                if node:
                    if result == '[':
                        result += bytes(node.val)
                    else:
                        result += ',' + bytes(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    result += ',#'
        while result[-1] == '#':
            result = result[:-2]
        result += ']'
        return result
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        q = []
        index = 0
        serializedArr = data[1:-1].split(',')
        for i in xrange(len(serializedArr)):
            if serializedArr[i] != '#':
                node = TreeNode(serializedArr[i])
                if i != 0 and i % 2 == 1:
                    q[index].left = node
                elif i != 0 and i % 2 == 0:
                    q[index].right = node
                q.append(node)
            if i != 0 and i % 2 == 0:
                index += 1
        return q[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))