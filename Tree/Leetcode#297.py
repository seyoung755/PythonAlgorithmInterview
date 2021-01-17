# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Codec:

    def serialize(self, root):
        Q = collections.deque([root])
        result = ['#']
        
        while Q:
            node = Q.popleft()
            
            if node:
                Q.append(node.left)
                Q.append(node.right)
                
                result.append(str(node.val))
            
            else:
                result.append('#')
    
        print(result)
        return ' '.join(result)

    def deserialize(self, data):
        
        if data == '# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        Q = collections.deque([root])
        index = 2
        
        while Q:
            node = Q.popleft()
            
            # 왼쪽 자식은 무조건 짝수
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                Q.append(node.left)
            index += 1
            
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                Q.append(node.right)
            index += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))