class Solution(object):
    def findClosestElements(self, arr, k, x):
        result = []
        if not arr or len(arr) == 0:
            return result

        l = 0
        h = len(arr) - 1
        while l + 1 < h:
            m = (l + h) / 2
            if arr[m] <= x:
                l = m
            else:
                h = m

        while len(result) < k:
            numL = abs(arr[l] - x) if l >= 0 else None
            numH = abs(arr[h] - x) if h < len(arr) else None

            if numL is not None and numH is not None:
                if numL <= numH:
                    result.append(arr[l])
                    l -= 1
                else:
                    result.append(arr[h])
                    h += 1
            elif numL is not None:
                result.append(arr[l])
                l -= 1
            elif numH is not None:
                result.append(arr[h])
                h += 1
            else:
                break

        return sorted(result)
