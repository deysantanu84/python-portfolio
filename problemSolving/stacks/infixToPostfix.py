# Given string A denoting an infix expression. Convert the infix expression into postfix expression.
# String A consists of ^, /, *, +, -, (, ) and lowercase english alphabets where
# lowercase english alphabets are operands and ^, /, *, +, - are operators.
# Find and return the postfix expression of A.
# NOTE:
# ^ has highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.
# 1 <= length of the string <= 500000
class Conversion:
    def __init__(self):
        self.stack = []
        self.result = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infixToPostfix(A):
    stack = []
    result = []
    operatorPrecedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for ch in A:
        if ch.isalpha():
            result.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while len(stack) and stack[-1] != '(':
                result.append(stack.pop())

            if len(stack) and stack[-1] != '(':
                return -1
            else:
                stack.pop()

        else:
            while len(stack) and operatorPrecedence[ch] <= operatorPrecedence[stack[-1]]:
                result.append(stack.pop())

            stack.append(ch)

    while len(stack):
        result.append(stack.pop())

    return "".join(result)


print(infixToPostfix("x^y/(a*z)+b"))  # "xy^az*/b+"
print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))  # "abcd^e-fgh*+^*+i-"
