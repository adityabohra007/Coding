class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        self.map = {}
        for word in dict:
            length = len(word)
            for i in xrange(length):
                for j in xrange(i+1, length+1):
                    s = word[i:j]
                    if s not in self.map:
                        self.map[s] = [word]
                    elif self.map[s][-1] != word:
                        self.map[s].append(word)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        if str in self.map:
            return self.map[str]
        return []