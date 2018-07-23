class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters is None or len(letters) == 0 or target == "":
            return ""
        for c in letters:
            if c > target:
                return c
        return letters[0]
