# #2265 - 2265. Count Nodes Equal to Average of Subtree

## Problem Metadata

| Metric | Value |
| :--- | :--- |
| **Difficulty** | `Medium` |
| **Language** | `Python3` |
| **Runtime** | `48` |
| **Memory** | `19788000` |
| **Topic Tags** | `Tree, Depth-First Search, Binary Tree` |
| **Date** | `2026-09-10 17:57` |

## Solution

```python3
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            
            if node.val == curr_sum // curr_count:
                self.count += 1
                
            return (curr_sum, curr_count)
        
        dfs(root)
        return self.count
```

---
*Generated automatically by [RG Sync](https://github.com).*