# Given a digit string A, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 0 -> 0, 1 -> 1, 2 -> abc, 3 -> def, 4 -> ghi, 5 -> jkl
# 6 -> mno, 7 -> pqrs, 8 -> tuv, 9 -> wxyz
# The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.
# NOTE: Make sure the returned strings are lexicographically sorted.
# 1 <= |A| <= 10
# Return a string array denoting the possible letter combinations.
class Solution(object):
    def backtracking(self, A, result, subset, index, mapping):
        if len(A) == index:
            result.append(''.join(subset))
            return

        for i in mapping[A[index]]:
            subset.append(i)
            self.backtracking(A, result, subset, index + 1, mapping)
            subset.pop()

    def letterPhone(self, A):
        if A == '':
            return []

        mapping = {'0': ['0'],
                   '1': ['1'],
                   '2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        result = []
        self.backtracking(A, result, [], 0, mapping)
        return result


obj = Solution()
print(obj.letterPhone("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(obj.letterPhone("012"))  # ["01a", "01b", "01c"]
