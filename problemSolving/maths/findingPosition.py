# Given an integer A which denotes the number of people standing in the queue.
# A selection process follows a rule where people standing on even positions are selected.
# Of the selected people a queue is formed and again out of these only people on even position are selected.
# This continues until we are left with one person.
# Find and return the position of that person in the original queue.
# 1 <= A <= 10^9
# A = 10 -- 8
# Initially, people at 2, 4, 6, 8, 10 position are selected.
# Then 4, 8 are selected since 4 at 2nd position and 8 at 4th position in the new queue.
# Finally 8 is selected.
# A = 5 -- 4
# Initially, people at 2, 4 positions are selected.
# Finally, 4 is selected.
from math import log2


def findingPosition2(A):
    result = []
    for i in range(A):
        result.append(i + 1)
    while len(result) > 1:
        del result[::2]
    return result[0]


def findingPosition(A):
    return 2**int(log2(A))


print(findingPosition(10))  # 8
print(findingPosition(5))  # 4
print(findingPosition(671982))  # 524288
