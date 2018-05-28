"""
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,2,3,4,5,6].
"""
class Vector2D(object):
    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.vec2d = vec2d

    def next(self):
        self.col += 1
        return self.vec2d[self.row][self.col - 1]

    def hasNext(self):
        while self.row < len(self.vec2d):
            if self.col < len(self.vec2d[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())