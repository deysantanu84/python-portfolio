# Given an expression string A, examine whether the pairs and the orders
# of "{","}", "(",")", "[","]" are correct in A.
# Refer to the examples for more clarity.
# 1 <= |A| <= 100
# Return 0, if the parenthesis sequence is not balanced.
# Return 1, if the parenthesis sequence is balanced.
def balancedParenthesis(A):
    stack = []
    pairDict = {'(': ')', '{': '}', '[': ']'}

    for item in A:
        if item in pairDict:
            stack.append(item)

        elif len(stack) == 0 or pairDict[stack.pop()] != item:
            return 0

    if len(stack) == 0:
        return 1

    else:
        return 0


print(balancedParenthesis('{([])}'))  # 1
print(balancedParenthesis('(){'))  # 0
print(balancedParenthesis('()[]'))  # 1
