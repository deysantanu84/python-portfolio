# Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
# Check whether A has redundant braces or not.
# NOTE: A will be always a valid expression.
# 1 <= |A| <= 10^5
# Return 1 if A has redundant braces, else return 0.
def redundantBraces(A):
    stack = []

    for ch in A:
        if ch == ')':
            top = stack[-1]
            stack.pop()

            flag = True

            while top != '(':
                if top == '+' or top == '-' or top == '*' or top == '/':
                    flag = False

                top = stack[-1]
                stack.pop()

            if flag:
                return 1

        else:
            stack.append(ch)

    return 0


print(redundantBraces("((a+b))"))  # 1
print(redundantBraces("(a+(a+b))"))  # 0
