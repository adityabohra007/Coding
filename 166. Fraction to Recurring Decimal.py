class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        answer = []
        map = {}
        if (numerator == 0):
            return "0"

        if ((numerator > 0) ^ (denominator > 0)):
            answer.append("-")

        nume = abs(numerator)
        deno = abs(denominator)

        #solve integral part
        answer.append(str(nume / deno))

        remainder = nume % deno
        if remainder == 0:
            return ''.join(answer)

        #solve fractional part
        answer.append(".")

        while (remainder != 0):
            if remainder in map:
                idx = map.get(remainder)
                return ''.join(answer[:idx]) + "(" + ''.join(
                    answer[idx:]) + ")"

            map[remainder] = len(answer)
            nume = remainder * 10
            answer.append(str(nume / deno))
            remainder = nume % deno

        return ''.join(answer)
