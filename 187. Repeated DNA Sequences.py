class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) < 10:
            return []
        hash = {}
        result = []
        for i in xrange(len(s)-9):
            dna = s[i:i+10]
            encode = self.encode(dna)
            if encode in hash:
                if hash[encode] == 1:
                    result.append(dna)
                hash[encode] += 1
            else:
                hash[encode] = 1
        return result

    def encode(self, dna):
        sum = 0
        for c in dna:
            if c == 'A':
                sum = 4*sum
            elif c == 'C':
                sum = 4*sum + 1
            elif c == 'G':
                sum = 4*sum + 2
            else:
                sum = 4*sum + 3
        return sum
