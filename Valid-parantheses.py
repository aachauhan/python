class Solution:
    def isValid(self, s: str) -> bool:
        l = 0
        #input ()
        #output true
#it is given, a input string is only valid when opened brackes is
# closed by same type of bracket, there are three types '(' '{' '[, and opened bracket must be closed in the correct order
#() - parantheses in - out, no other input, in out in correct order - return true
#()[]{} - p in out, in correct order, * 3 - return true#
