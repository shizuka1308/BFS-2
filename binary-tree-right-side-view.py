# Explanation:
# The solution performs a level-order traversal (BFS), appending the last node's value from each level to the result list, 
# which represents the right side view of the tree.

# Time Complexity: O(N), where N is the number of nodes in the tree, as each node is visited once.
# Space Complexity: O(N) for the queue, which stores nodes at each level during traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root]) # Initialize queue with the root
        result = []
        while queue:
            level_size = len(queue) #no. of nodes at current level
            for i in range(level_size):
                node = queue.popleft() #get the front nodes

                if i == level_size - 1: #last node in the level
                    result.append(node.val)
                
                #add left and right child to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
        return result

