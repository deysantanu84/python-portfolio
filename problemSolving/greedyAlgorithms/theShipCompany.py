# The local ship renting service has a special rate plan:
# It is up to a passenger to choose a ship.
# If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
# The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one,
# and so on up to A-th person.
# You need to tell the maximum and the minimum money that the ship company can earn if all A passengers
# buy tickets.
# 1 ≤ A ≤ 3000
# 1 ≤ B ≤ 1000
# 1 ≤ C[i] ≤ 1000
# It is guaranteed that there are at least A empty seats in total.
# First argument is a integer A denoting the number of passengers in the queue.
# Second argument is a integer B denoting the number of ships.
# Third argument is an integer array C of size B where C[i] denotes the number of empty seats in
# the i-th ship before the ticket office starts selling tickets.
# Return an array of size 2 denoting the maximum and minimum money that the ship company can earn.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        result = []
        maxVal = 0
        minVal = 0

        minQueue = sorted(C)
        maxQueue = sorted(C, reverse=True)

        while A:
            temp1 = maxQueue.pop(0)
            maxVal += temp1
            if temp1 - 1:
                maxQueue.append(temp1 - 1)
                maxQueue.sort(reverse=True)

            temp2 = minQueue.pop(0)
            minVal += temp2
            if temp2 - 1:
                minQueue.append(temp2 - 1)
                minQueue.sort()

            A -= 1

        result.append(maxVal)
        result.append(minVal)

        return result


sol = Solution()
print(sol.solve(4, 3, [2, 1, 1]))  # [5, 5]
print(sol.solve(4, 3, [2, 2, 2]))  # [7, 6]
