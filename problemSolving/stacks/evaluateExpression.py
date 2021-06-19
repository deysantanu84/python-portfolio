# An arithmetic expression is given by a character array A of size N.
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each character may be an integer or an operator.
# 1 <= N <= 10^5
def evaluateExpression(A):
    stack = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }

    for item in A:
        if item in operators:
            b = stack.pop()
            a = stack.pop()
            value = operators[item](a, b)
            stack.append(value)

        else:
            stack.append(int(item))

    return stack[0]


print(evaluateExpression(["2", "1", "+", "3", "*"]))  # 9
print(evaluateExpression(["4", "13", "5", "/", "+"]))  # 6
