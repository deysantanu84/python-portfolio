# Given a string A consisting of lowercase English alphabets and parentheses '(' and ')'.
# Remove the minimum number of invalid parentheses in order to make the input string valid.
# Return all possible results.
# You can return the results in any order.
# 1 <= length of the string <= 20
# Return all possible strings after removing the minimum number of invalid parentheses.
class Solution:
    def backtracking(self, lefts, rights, A, index, currStr, result, leftsToRemove, rightsToRemove):
        if index == len(A):
            if lefts == rights and leftsToRemove == 0 \
                    and rightsToRemove == 0 and currStr not in result:
                result.append(currStr)
            return

        if A[index] == '(':
            if leftsToRemove > 0:
                self.backtracking(lefts, rights, A, index + 1, currStr,
                                  result, leftsToRemove - 1, rightsToRemove)
            self.backtracking(lefts + 1, rights, A, index + 1, currStr + '(',
                              result, leftsToRemove, rightsToRemove)

        elif A[index] == ')':
            if (lefts == 0 or lefts >= rights) and rightsToRemove > 0:
                self.backtracking(lefts, rights, A, index + 1, currStr,
                                  result, leftsToRemove, rightsToRemove - 1)

            if lefts > rights:
                self.backtracking(lefts, rights + 1, A, index + 1, currStr + ')',
                                  result, leftsToRemove, rightsToRemove)

        else:
            self.backtracking(lefts, rights, A, index + 1, currStr + A[index],
                              result, leftsToRemove, rightsToRemove)

    def removeInvalidParentheses(self, A):
        result = []
        rightsToRemove = 0
        lefts = 0
        
        for i in range(len(A)):
            if A[i] == '(':
                lefts += 1
            
            elif A[i] == ')':
                if lefts > 0:
                    lefts -= 1
                
                else:
                    rightsToRemove += 1
        
        leftsToRemove = lefts

        self.backtracking(0, 0, A, 0, '', result, leftsToRemove, rightsToRemove)
        
        if not result:
            result.append('')

        return result


obj = Solution()
print(obj.removeInvalidParentheses("()())()"))  # ["()()()", "(())()"]
print(obj.removeInvalidParentheses("(a)())()"))  # ["(a)()()", "(a())()"]
