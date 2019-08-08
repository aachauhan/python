# Problem Name is &&& Second Smallest &&& PLEASE DO NOT REMOVE THIS LINE.

"""
 Instructions to candidate.
  1) Run this code in the REPL to observe its behaviour. The
     execution entry point is main().
  2) Consider adding some additional tests in doTestsPass().
  3) Implement secondSmallest() correctly.
  4) If time permits, some possible follow-ups.
"""


def secondSmallest(x):
    """ Returns second smallest element in the array x. Returns nothing if array has less than 2 elements. """
    # todo: implement here
    # if the array is more than two elements
    secondSmall = 0;
    if (len(x) > 1):
        for i in range(len(x)):
            if (x[i] > secondSmall):
                secondSmall = x[i]
            return secondSmall
    else:
        return False

    ##reiterate through the given array
    ##spew out the second smallest
    # else return nothing

    # 0, 2, 1
    # 0, 1
    # 1, 2, 3
    # 3,2,1

    return


def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    testArrays = [[0], [0, 1], [3, 2, 1]]
    testAnswers = [None, 1, 2]

    for i in range(len(testArrays)):
        if not (secondSmallest(testArrays[i]) == testAnswers[i]):
            return False

    return True


if __name__ == "__main__":
    if (doTestsPass()):
        print("All tests pass")
    else:
        print("Not all tests pass")