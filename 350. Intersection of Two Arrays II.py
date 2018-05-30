class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                result.append(nums1[n1])
                n1 += 1
                n2 += 1
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        return result
