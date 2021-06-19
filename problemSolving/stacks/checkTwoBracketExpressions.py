# Given two strings A and B. Each string represents an expression
# consisting of lowercase english alphabets, '+', '-', '(' and ')'.
# The task is to compare them and check if they are similar. If they are similar return 1 else return 0.
# NOTE: It may be assumed that there are at most 26 operands from 'a' to 'z' and every operand appears only once.
# 1 <= length of the each String <= 100
def localSign(string, index):
    if index == 0:
        return True

    if string[index - 1] == '-':
        return False

    return True


def evaluateExpression(string, vector, add):
    stack = [True]
    index = 0

    while index < len(string):
        if string[index] == '+' or string[index] == '-':
            index += 1
            continue

        if string[index] == '(':
            if localSign(string, index):
                stack.append(stack[-1])
            else:
                stack.append(not stack[-1])

        elif string[index] == ')':
            stack.pop()
        else:
            if stack[-1]:
                vector[ord(string[index]) - ord('a')] += (1 if add else -1) \
                    if localSign(string, index) else (-1 if add else 1)

            else:
                vector[ord(string[index]) - ord('a')] += (-1 if add else 1) \
                    if localSign(string, index) else (1 if add else -1)

        index += 1


def checkTwoBracketExpressions(A, B):
    vector = [0 for _ in range(26)]
    evaluateExpression(A, vector, True)
    evaluateExpression(B, vector, False)

    for i in range(26):
        if vector[i] != 0:
            return 0

    return 1


print(checkTwoBracketExpressions("-(a+b+c)", "-a-b-c"))  # 1
print(checkTwoBracketExpressions("a-b-(c-d)", "a-b-c-d"))  # 0
