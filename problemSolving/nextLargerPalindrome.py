# Given an positive integer A, find the next larger palindrome of the integer
import unittest


def nextLargerPalindrome(A):
    N = len(str(A))
    firstHalf = str(A)[:N//2]
    firstHalfMirror = firstHalf[-1::-1]
    hasMiddleDigit = N % 2

    if hasMiddleDigit:
        middleDigit = str(A)[N//2]
        secondHalf = str(A)[(N//2)+1:]
    else:
        middleDigit = ''
        secondHalf = str(A)[(N//2):]

    if firstHalfMirror > secondHalf:
        result = firstHalf + middleDigit + firstHalfMirror

    else:
        if hasMiddleDigit:
            middleDigit = str(int(middleDigit) + 1)
            if int(middleDigit) == 10:
                middleDigit = '0'
                firstHalf = str(int(firstHalf) + 1)

        else:
            firstHalf = str(int(firstHalf) + 1)

        firstHalfMirror = str(firstHalf)[-1::-1]
        if firstHalf.endswith('0'):
            middleDigit = ''
        if firstHalf.endswith('00'):
            firstHalfMirror = firstHalfMirror[1:]
        result = firstHalf + middleDigit + firstHalfMirror

    return int(result)


# Test Cases
class evaluatorTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(nextLargerPalindrome(1234025), 1234321, "Should Be 1234321")

    def testCase2(self):
        self.assertEqual(nextLargerPalindrome(123769), 124421, "Should Be 124421")

    def testCase3(self):
        self.assertEqual(nextLargerPalindrome(999), 1001, "Should Be 1001")

    def testCase4(self):
        self.assertEqual(nextLargerPalindrome(9999), 10001, "Should Be 10001")

    def testCase5(self):
        self.assertEqual(nextLargerPalindrome(1234524), 1235321, "Should Be 1235321")

    def testCase6(self):
        self.assertEqual(nextLargerPalindrome(1239524), 1240421, "Should Be 1240421")


if __name__ == '__main__':
    unittest.main()
    """
    print(nextLargerPalindrome(1234025))  # 1234321
    print(nextLargerPalindrome(123769))  # 124421
    print(nextLargerPalindrome(999))  # 1001
    print(nextLargerPalindrome(9999))  # 10001
    print(nextLargerPalindrome(1234524))  # 1235321
    print(nextLargerPalindrome(1239524))  # 1240421
    """
