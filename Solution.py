class Solution:
    def __init__(self):
        print("in init")

    def reverse(self, x: int) -> int:
        s = str(x)
        result = list()
        count = len(s)
        index = 0

        if (s[0] != '-'):
            for i in range(len(s) - 1, -1, -1):
                # print(s[i])
                result.append(s[i])
        else:
            result.insert(0, '-')
            for i in range(len(s) - 1, 0, -1):
                # print(s[i])
                result.append(s[i])

        tempStr = [str(m) for m in result]
        res = int("".join(map(str, tempStr)))

        return (res)