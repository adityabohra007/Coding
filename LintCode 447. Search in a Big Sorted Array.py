class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        low = 0
        high = index

        while low + 1 < high:
            mid = (low + high) / 2
            if reader.get(mid) >= target:
                high = mid
            else:
                low = mid

        if reader.get(low) == target:
            return low
        elif reader.get(high) == target:
            return high
        else:
            return -1