# Boolean Expression Evaluator
# >>>>>
# Input: Keys and Values like a = 1, b = 6
# Input: Expression to be evaluated (a < 4) && (b > 3)
# Input: Expression to be evaluated ((a < 4) && (b > 3)) || ((a > 4) && !(b < 6))
# Output: true or false
#
# Input: Keys and Values like a = 1, b = 6, c = 10
# Input: Expression to be evaluated (a < 4 && b > 3 && c < 9) || (a > 4 && !(b < 6) || c > 10)
# Output: true or false
# <<<<<
import unittest


# Boolean Expression Evaluator Function
def evaluateExpression(expression, a, b, c=None):
    # Invalid argument check
    if 'c' in expression and c is None:
        print('[ERROR] Invalid arguments passed!!!')
        return -1

    # Convert && in expression to and
    if '&&' in expression:
        expression = expression.replace('&&', 'and')

    # Convert || in expression to or
    if '||' in expression:
        expression = expression.replace('||', 'or')

    # Convert ! in expression to not
    if '!' in expression:
        expression = expression.replace('!', 'not')

    # If all arguments a, b, c are part of the expression
    if c:
        return eval(expression, {'a': a, 'b': b, 'c': c})

    # If only arguments a and b are part of the expression
    else:
        return eval(expression, {'a': a, 'b': b})


# Test Cases
class evaluatorTests(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(evaluateExpression(a=1, b=6,
                                            expression='(a < 4) && (b > 3)'),
                         True,
                         "Should Be True")

    def testCase2(self):
        self.assertEqual(evaluateExpression(a=1, b=6,
                                            expression='(a > 4) && !(b < 6)'),
                         False,
                         "Should Be False")

    def testCase3(self):
        self.assertEqual(evaluateExpression(a=1, b=6,
                                            expression='((a < 4) && (b > 3)) || ((a > 4) && !(b < 6))'),
                         True,
                         "Should Be True")

    def testCase4(self):
        self.assertEqual(evaluateExpression(a=1, b=6,
                                            expression='((a < 4) && (b > 3)) && ((a > 4) && !(b < 6))'),
                         False,
                         "Should Be False")

    def testCase5(self):
        self.assertEqual(evaluateExpression(a=1, b=6, c=10,
                                            expression='a < 4 && b > 3 && c > 9'),
                         True,
                         "Should Be True")

    def testCase6(self):
        self.assertEqual(evaluateExpression(a=1, b=6, c=10,
                                            expression='a > 4 && !(b < 6) || c > 10'),
                         False,
                         "Should Be False")

    def testCase7(self):
        self.assertEqual(evaluateExpression(a=1, b=6, c=10,
                                            expression='(a < 4 && b > 3 && c > 9) || (a > 4 && !(b < 6) || c > 10)'),
                         True,
                         "Should Be True")

    def testCase8(self):
        self.assertEqual(evaluateExpression(a=1, b=6, c=10,
                                            expression='(a < 4 && b > 3 && c < 9) && (a > 4 && !(b < 6) || c > 10)'),
                         False,
                         "Should Be False")


if __name__ == '__main__':
    unittest.main()
