# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Codec:

    def serialize(self, root, result = []):
        
        Q = collections.deque([root])
        sw = 0
        
        while Q:
            node = Q.popleft()
            
            if node:
                
                if sw == 0:
                    Q.append(node.left)
                    Q.append(node.right)
                    result.append(node.val)
                else:
                    result.append(node.val)
                
            else:
                result.append('null')
                sw = 1
            
        # print(result)
        return result
        

        
        
        
        

    def deserialize(self, data):
        node = TreeNode()
        
        Q = collections.deque([])
        # root = TreeNode(data.pop(0))
        root = TreeNode(data.pop(0))
        
        Q.append(root)
    
        while Q:
            
            
            node = Q.popleft()
            
            value = data.pop(0)
            if value == 'null':
                node = TreeNode()
            else:
                node = TreeNode(value)
            
            # print(node)
            
            
            if node:

                Q.append(node.left)
                Q.append(node.right)
            
            
            
            # if not root.left:
            #     root.left = node.left
            # elif not root.right:
            #     root.right = node.right
            
            


            print(root)
            
#         root = TreeNode(data.pop(0))
#         root.left = TreeNode(data.pop(0))
        
        return 0

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

