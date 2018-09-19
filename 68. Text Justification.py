class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if words is None or len(words) == 0 or maxWidth == 0:
            return []
        result = []
        line = []
        l = 0
        for w in words:
            if len(w) + len(line) + l <= maxWidth:
                l += len(w)
                line.append(w)
            else:
                result.append(self.helper(line, maxWidth))
                l = len(w)
                line = [w]
        if line:
            result.append(self.helper_last_line(line, maxWidth))
        return result

    def helper(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        total_word_length = sum(len(w) for w in line)
        s = line[0]
        space_total = len(line) - 1
        for i, w in enumerate(line[1:]):
            if i < (maxWidth - total_word_length) % space_total:
                s += " " + " " * ((maxWidth - total_word_length) / space_total) + w
            else:
                s += " " * ((maxWidth - total_word_length) / space_total) + w
        return s

    def helper_last_line(self, line, maxWidth):
        s = " ".join(line)
        return s + " " * (maxWidth - len(s))