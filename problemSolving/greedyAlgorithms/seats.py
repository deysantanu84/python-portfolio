# There is a row of seats represented by string A.
# Assume that it contains N seats adjacent to each other.
# There is a group of people who are already seated in that row randomly.
# i.e. some are sitting together & some are scattered.
# An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
# Now your target is to make the whole group sit together i.e. next to each other,
# without having any vacant seat between them in such a way that the
# total number of hops or jumps to move them should be minimum.
# In one jump a person can move to the adjacent seat (if available).
# NOTE: 1. Return your answer modulo 10^7 + 3.
# 1 <= N <= 1000000
# A[i] = 'x' or '.'
# First and only argument is a string A of size N.
# Return an integer denoting the minimum number of jumps required.
class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        N = len(A)
        position = []

        for i in range(N):
            if A[i] == 'x':
                position.append(i)

        posLen = len(position)

        if not posLen:
            return 0

        if posLen & 1:
            median = position[posLen//2]
        else:
            median = (position[(posLen//2) - 1] + position[posLen//2]) // 2

        hopsCount = 0

        if A[median] == 'x':
            emptySeats = median - 1
        else:
            emptySeats = median

        for index in range(median - 1, -1, -1):
            if A[index] == 'x':
                hopsCount = (hopsCount + emptySeats - index) % (10**7 + 3)
                emptySeats -= 1

        emptySeats = median + 1

        for index in range(median + 1, N):
            if A[index] == 'x':
                hopsCount = (hopsCount + index - emptySeats) % (10**7 + 3)
                emptySeats += 1

        return hopsCount % (10**7 + 3)


sol = Solution()
print(sol.seats("....x..xx...x.."))  # 5
print(sol.seats("....xxx"))  # 0
