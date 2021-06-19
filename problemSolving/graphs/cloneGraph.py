# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 1 <= Number of nodes <= 10^5
# First and only argument is a node A denoting the root of the undirected graph.
# Return the node denoting the root of the new clone graph.
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        cloneDict = {node.label: UndirectedGraphNode(node.label)}
        queue = [node]

        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor.label not in cloneDict:
                    cloneDict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)

                cloneDict[curr.label].neighbors.append(cloneDict[neighbor.label])

        return cloneDict[node.label]


sol = Solution()
G = UndirectedGraphNode(1)
G1 = UndirectedGraphNode(3)
G2 = UndirectedGraphNode(2)
G3 = UndirectedGraphNode(4)
G4 = UndirectedGraphNode(5)
G5 = UndirectedGraphNode(6)
G.neighbors = [G1, G2, G3]
G3.neighbors = [G4, G5]
sol.cloneGraph(G)

G = UndirectedGraphNode(1)
G1 = UndirectedGraphNode(3)
G2 = UndirectedGraphNode(4)
G3 = UndirectedGraphNode(2)
G4 = UndirectedGraphNode(5)
G5 = UndirectedGraphNode(7)
G6 = UndirectedGraphNode(6)
G.neighbors = [G1, G2]
G1.neighbors = [G3]
G2.neighbors = [G4, G5, G6]
sol.cloneGraph(G)
