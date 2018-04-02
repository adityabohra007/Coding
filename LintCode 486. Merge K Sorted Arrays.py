class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if len(arrays) == 1:
            return arrays[0]

        left = self.mergekSortedArrays(arrays[:len(arrays) / 2])
        right = self.mergekSortedArrays(arrays[len(arrays) / 2:])
        return self.merge2Arrays(left, right)

    def merge2Arrays(self, arr1, arr2):
        ret = []
        n1, n2 = 0, 0

        while n1 < len(arr1) and n2 < len(arr2):
            if arr1[n1] < arr2[n2]:
                ret.append(arr1[n1])
                n1 += 1
            else:
                ret.append(arr2[n2])
                n2 += 1

        while n1 < len(arr1):
            ret.append(arr1[n1])
            n1 += 1

        while n2 < len(arr2):
            ret.append(arr2[n2])
            n2 += 1

        return ret
