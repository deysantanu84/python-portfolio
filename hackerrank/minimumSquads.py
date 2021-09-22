# Find the minimum number of squads that you can send to battle meeting the given constraints
# You are assembling a rebel army to fight against the Galactic Empire. For this you have invited people from
# several influential families to join your army. You want to create squads that can be sent to battle the Empire.
# However you find that as soon as you add a person with their child, grandchild or any descendant in the same squad,
# they begin to give orders to the descendant and the squad quickly falls apart. Your goal is to find the minimum
# number of such squads that you can create that do not have this problem.
# In your army, each person has a maximum of 1 parent. A person may have one or more ancestors that may be direct or
# indirect. X is an ancestor of Y if at least one of the following is true:
# X is a parent of Y (direct ancestor)
# If X is a parent of Z, and Z is a parent of Y, then X is an indirect ancestor of Y. Indirect ancestor is transitive
# through any number of levels.
# No two people will ever be mutual ancestors, and no person is a parent of themselves. Determine the minimum
# number of squads that must be formed so that no person is in the same squad with their ancestor, direct or indirect.
# Example:
# parents = [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
# labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Each person in parents represents a person and each element represents a parent of that person, or -1 if there
# is none. The graph of ancestors is below using zero based indexing. All labels are the indices within parents.
# Graph: 0 -> 3 -> 5    8 -> 1
#                         -> 6 -> 2
#                              -> 9 -> 7 -> 4
# From the graph, a possible grouping is: [0, 8], [3, 1, 6], [5, 2, 9], [7], [4]
# A minimum of 5 squads are needed to satisfy all conditions.
# parents[i] represents the parent of ith person or -1 if there is none.
def getDepth(node, children):
    depth = 0
    for child in children[node]:
        depth = max(depth, getDepth(child, children))

    return depth + 1


def minimumSquads(parents):
    result = 0
    N = len(parents)
    children = [[] for _ in range(N + 1)]

    for index in range(N):
        if parents[index] != -1:
            children[parents[index]].append(index)

    for index in range(N):
        if parents[index] == -1:
            result = max(result, getDepth(index, children))

    return result


print(minimumSquads([-1, 0, 1]))  # 3 ([0], [1], [2])
print(minimumSquads([1, -1, 3, -1]))  # 2 ([0, 2], [1, 3])
