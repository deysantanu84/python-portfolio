# Given string A denoting an infix expression. Convert the infix expression into postfix expression.
# String A consists of ^, /, *, +, -, (, ) and lowercase english alphabets where
# lowercase english alphabets are operands and ^, /, *, +, - are operators.
# Find and return the postfix expression of A.
# NOTE:
# ^ has highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.
# 1 <= length of the string <= 500000
def infixToPostfix(A):
    stack = ['N']
    result = ''
    N = len(A)
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': -1, ')': -1}

    for i in range(N):
        if 'a' <= A[i] <= 'z' or 'A' <= A[i] <= 'Z':
            result += A[i]

        elif A[i] == '(':
            stack.append('(')

        elif A[i] == ')':
            while stack[-1] != 'N' and stack[-1] != '(':
                result += stack.pop()

            if stack[-1] == '(':
                stack.pop()

        else:
            while stack[-1] != 'N' and precedence[A[i]] <= precedence[stack[-1]]:
                result += stack.pop()

            stack.append(A[i])

    while stack[-1] != 'N':
        result += stack.pop()

    return result


print(infixToPostfix("x^y/(a*z)+b"))  # "xy^az*/b+"
print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))  # "abcd^e-fgh*+^*+i-"
