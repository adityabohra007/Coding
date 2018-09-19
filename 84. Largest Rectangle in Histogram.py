class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights is None or len(heights) == 0:
            return 0
        result = 0
        stack = []
        for i, h in enumerate(heights + [-1]):
            while stack and heights[stack[-1]] > h:
                pop_index = stack.pop()
                left_index = stack[-1] if stack else -1
                width = i - left_index - 1
                result = max(result, width*heights[pop_index])
            stack.append(i)
        return result