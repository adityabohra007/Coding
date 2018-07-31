class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        result = []
        if logs is None or len(logs) == 0:
            return result
        logArr = sorted(logs, cmp=self.cmpHelper)
        tmp = []
        for log in logArr:
            index = log.find(" ")
            if log[index+1].isalpha():
                result.append(log)
        for log in logs:
            index = log.find(" ")
            if not log[index+1].isalpha():
                result.append(log)
        return result
    
    def cmpHelper(self, a, b):
        i = a.find(" ")
        j = b.find(" ")
        titleA = a[:i]
        conA = a[i+1:]
        titleB = b[:j]
        conB = b[j+1:]
        if conA != conB:
            return -1 if conA < conB else 1
        return -1 if titleA < titleB else 1