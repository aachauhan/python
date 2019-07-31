class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        result = list()
        count = len(s)
        index = 0

        # new_index = max(0, min(new_index, len(mylist)-1))

        # new_index = max(0, min(new_index, len(mylist)-1))

        if s[0] != '-':
            for i in range(len(s) - 1, -1, -1):
                result.append(s[i])
        else:
            result.insert(0, '-')
            for i in range(len(s) - 1, 0, -1):
                result.append(s[i])

        tempStr = [str(m) for m in result]
        res = int("".join(map(str, tempStr)))

        if res > 2147483647 or res < -2147483647:
            return 0
        else:
            return res