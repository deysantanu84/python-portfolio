# A subsequence is a sequence that can be derived from another sequence by deleting some elements
# without changing the order of the remaining elements. For example, the sequence {2, 3, 5} is a
# subsequence of {1, 2, 3, 4, 5} obtained after removal of elements {1, 4}.
# Given is an array of integers A of size N. An array of size N can have (2^N - 1) number of
# non empty subsequences.
# For the given function:
#
#  solve (int subsequence[]) {
#     int count[];    //array initialised to 0.
#     for(int i = 0; i &amp;lt; subsequence.length; i++) {
#         number = subsequence[i];
#         for(int j = 2; j &amp;lt;= number; j++) {
#             if(number % j == 0) {
#                 count[j]++;
#                 if(count[j] == subsequence.length)  return 0;
#             }
#         }
#     }
#     return 1;
# }
# If all the subsequences of the array A are passed in the above function.
# What will be the bitwise OR of all the returned values from the given function.
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# The only argument given is the integer array A.
# Return the bitwise OR of all the returned values.
class Solution:
    def euclidean_gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = A[0]
        for i in range(1, len(A)):
            result = self.euclidean_gcd(A[i], result)

        if result == 1:
            return 1
        else:
            return 0


sol = Solution()
print(sol.solve([1, 2, 3]))  # 1
print(sol.solve([2, 4, 6, 8]))  # 0
