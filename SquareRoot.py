# Problem Name is &&& Square Root &&& PLEASE DO NOT REMOVE THIS LINE.


"""
Instructions to candidate
  * This is **NOT** a math problem. You are required to code up a simple mathematical technique to find the square root of a number.
  * The Newton-Raphson method can be used to find the square root of a number N as follows
      ** Make an initial guess
      ** Update the guess using the below formula
      ** New Estimate = Current Estimate - ( F(Current Estimate) / F'(Current Estimate) ), where
         F(Current Estimate) = Current Estimate * Current Estimate - N
         F'(Current Estimate) = 2*Current Estimate
      ** Repeat till you are close enough
  * Run this code in the REPL to observe its behaviour. The
     execution entry point is main().
  * Consider adding some additional tests in doTestsPass().
"""


def squareRoot(x):
    """ Returns the square root of x """
    # todo : implement here
    threshold = 0.001
    initGuess = x / 2
    iterator = 100
    # x = initGuess - (initGuess * initGuess - N) / (2 * initGuess)

    #while (iterator > 0):

    return (0)


def doTestsPass():
    """ Returns True if all tests pass. Otherwise returns False """
    doPass = True
    inputs = [2, 4, 100]
    expected_values = [1.41421, 2, 10]
    threshold = 0.001
    for i in range(0, len(inputs)):
        if abs(squareRoot(inputs[i]) - expected_values[i]) > threshold:
            print("Failed for %f - expected = %f, found = %f" % (inputs[i], expected_values[i], squareRoot(inputs[i])))
            doPass = False
    if doPass:
        print("All tests pass\n")
    return doPass


if __name__ == "__main__":
    doTestsPass()