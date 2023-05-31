class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        output = []

        if (numerator < 0) ^ (denominator < 0):
            output.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        output.append(str(numerator // denominator))

        remainder = numerator % denominator
        if not remainder:
            return "".join(output)

        output.append(".")

        met = dict()
        while remainder != 0:
            if remainder in met:
                output.insert(met[remainder], "(")
                output.append(")")
                break

            met[remainder] = len(output)
            remainder *= 10
            output.append(str(remainder // denominator))
            remainder %= denominator


        return "".join(output)