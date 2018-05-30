class Solution1:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        result = []
        i, j, index = 0, 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if index == 0 or result[index - 1] != nums1[i]:
                    result.append(nums1[i])
                    index += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result

"""
Solution2
"""
class Solution2:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):

        return list(set(nums1) & set(nums2))

"""
Solution 3
"""
class Solution3:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        p1, p2 = 0, 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if len(result) == 0 or (len(result) > 0
                                        and result[-1] != nums1[p1]):
                    result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return result