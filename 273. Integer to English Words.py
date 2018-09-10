in_twenty = [
    "",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen"]
in_hundred = [
    "",
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety"]
over_thousand = [
    "",
    "Thousand",
    "Million",
    "Billion"]


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = ""
        i = 0
        while num > 0:
            num, rem = divmod(num, 1000)
            rem_to_string = self.helper(rem)
            if rem_to_string:
                result = rem_to_string + " " + over_thousand[i] + " " + result
            i += 1
        return result.strip()

    def helper(self, rem):
        result = ""
        if rem < 20:
            result = in_twenty[rem]
        elif rem < 100:
            n, r = divmod(rem, 10)
            result = in_hundred[n] + " " + in_twenty[r]
        else:
            n, r = divmod(rem, 100)
            result = in_twenty[n] + ' Hundred ' + self.helper(r)
        return result.strip()


