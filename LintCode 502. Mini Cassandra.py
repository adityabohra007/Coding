"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""

from collections import OrderedDict
class MiniCassandra:
    
    def __init__(self):
        self.hash = {}

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        if raw_key not in self.hash:
            self.hash[raw_key] = OrderedDict()
        self.hash[raw_key][column_key] = column_value

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        result = []
        if raw_key not in self.hash:
            return result
        
        self.hash[raw_key] = OrderedDict(sorted(self.hash[raw_key].items()))
        for k, v in self.hash[raw_key].items():
            if k >= column_start and k <= column_end:
                result.append(Column(k,v))
        return result
