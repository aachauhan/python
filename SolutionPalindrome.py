class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert the integer to string
        # reverse the string
        # check if reversed string is equal to original
        # is palindrome if last statement was right

        strPre = str(x)

        reversedstr = strPre[::-1]

        if (reversedstr == strPre):
            return True
        else:
            return False