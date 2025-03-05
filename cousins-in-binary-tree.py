# Explanation:
# The solution performs a level-order traversal (BFS) of the binary tree, checking if the two nodes x and y are at the same level 
# and have different parents. If both conditions are met, they are cousins.

# Time Complexity: O(N), where N is the number of nodes in the tree, because we visit each node once.
# Space Complexity: O(N) for the queue, which stores nodes at each level of the tree.
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return []
        # Initialize the queue for BFS and insert the root node along with its parent (None)
        queue = deque([(root, None)])
        # traverse tree level by level
        while queue:
            level_size = len(queue)
            found_x, found_y = False, False
            # Process all nodes at the current level
            for i in range(level_size):
                node, parent = queue.popleft()
                # Check if current node is either x or y
                if node.val == x:
                    found_x = True
                    x_parent = parent # Save the parent of x
                if node.val == y:
                    found_y = True
                    y_parent = parent # Save the parent of x
                # Add children to the queue if they exist
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            # After processing the current level:
            # If both nodes are found and have different parents, they are cousins
            if found_x and found_y:
                return x_parent != y_parent
            # If we find one node but not the other, they can't be cousins
            if found_x or found_y:
                return False
        # If we exit the loop, it means one or both nodes were not found
        return False




        