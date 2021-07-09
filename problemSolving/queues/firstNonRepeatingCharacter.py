# Given a string A denoting a stream of lowercase alphabets.
# You have to make new string B. B is formed such that we have to find first non-repeating character
# each time a character is inserted to the stream and append it at the end to B.
# If no non-repeating character is found then append '#' at the end of B.
# 1 <= |A| <= 100000
# The only argument given is string A.
# Return a string B after processing the stream of lowercase alphabets A.
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        queue = []
        result = ''
        countDict = {}

        for i in range(len(A)):
            queue.append(A[i])
            if ord(A[i]) in countDict.keys():
                countDict[ord(A[i])] += 1
            else:
                countDict[ord(A[i])] = 1

            while len(queue):
                if countDict[ord(queue[0])] > 1:
                    queue.pop(0)
                else:
                    result += queue[0]
                    break

            if not len(queue):
                result += '#'

        return result


sol = Solution()
print(sol.solve("abadbc"))  # "aabbdd"
print(sol.solve("abcabc"))  # "aaabc#"
