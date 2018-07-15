class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hash = {}
        paragraph = paragraph.replace(",", '')
        paragraph = paragraph.replace("!", '')
        paragraph = paragraph.replace("?", '')
        paragraph = paragraph.replace("'", '')
        paragraph = paragraph.replace(";", '')
        paragraph = paragraph.replace(".", '')
        arr = paragraph.split(" ")
        for word in arr:
            word = word.lower()
            if word not in banned:
                hash[word] = hash[word]+1 if word in hash else 1

        hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        return hash[0][0]
