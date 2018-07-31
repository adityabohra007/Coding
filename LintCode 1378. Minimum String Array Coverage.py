from collections import defaultdict
class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """
    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        if len(allTags) < len(tagList):
            return -1
        result = len(allTags)+1
        need = defaultdict(int)
        for c in tagList:
            need[c] += 1
        missing = len(tagList)
        i = 0
        for j in xrange(len(allTags)):
            c = allTags[j]
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[allTags[i]] < 0:
                    need[allTags[i]] += 1
                    i += 1
                if j + 1 - i < result:
                    result = j + 1 - i
        return result if result != len(allTags)+1 else -1