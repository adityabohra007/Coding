class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """

    def twitchWords(self, str):
        # Write your code here
        if str is None or len(str) < 3:
            return []
        target = str[0]
        i, j = 0, 0
        result = []
        while j < len(str):
            while j < len(str) and str[j] == str[i]:
                j += 1
            if j - i >= 3:
                result.append([i, j-1])
            i = j
        return result
