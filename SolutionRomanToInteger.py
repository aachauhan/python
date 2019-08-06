class Solution:
    def romanToInt(self, s: str) -> int:
        # MCMXCIV
        # 1994 - 1000 - 900 - 90 - 4
        # IV - 4, IX - 9, XL - 40, XC - 90, CD - 400, CM - 900
        romanvalDict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        count = 0
        while count < len(s):
            sliced = s[count:count+2]
            # check if sliced is in specialdict
            if s[count:count+2] in romanvalDict:
                result += romanvalDict[s[count:count+2]]
            elif s[count] in romanvalDict:
                result += romanvalDict[s[count]]
            else:
                raise ValueError("Not a roman numeral")
            count = count + 1

        return result

        # iterate throught the string while checking the index and index + 1
        # for x in range(0, len(s)):
        # print(x)