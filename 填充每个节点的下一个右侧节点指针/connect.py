
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def create_tree(self, vals):
        if len(vals) == 0:
            return None

        que = []
        fill_left = True

        for val in vals:
            node = Node(val)

            if len(que) == 0:
                root = node
                que.append(node)
            elif fill_left:
                que[0].left = node
                if node:
                    que.append(node)
                fill_left =  False
            else:
                que[0].right = node
                if node:
                    que.append(node)
                que.pop(0)
                fill_left = True
        return root 


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root 

        stack = [root]
        res = []

        while(stack):
            curSize = len(stack)

            for i in range(curSize):
                node = stack.pop(0)
                
                if i < curSize - 1:
                    node.next = stack[0]

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return root

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root

        start = root

        # 在当前层构造好链表后，再去构建下一层的链表，同时由于是完美二叉树，只要起始节点的左节点存在，那么当前层就存在
        while(start.left): # 第N+1层
            head = start   # 第N层
            while(head): 
                # 根据第N层构建第N+1链表
                head.left.next = head.right  # 这是直接链接的情况

                if head.next:  # 根据第N层构建两个子树（不同根节点）的链接
                    head.right.next = head.next.left 
                head = head.next # 在一层中移动
            start = start.left # 往每一次层移动

        return root


if __name__ == "__main__":
    vals = [1,2,3,4,5,6,7]
    n = Node()
    root = n.create_tree(vals)
    s =  Solution()
    print(s.connect(root))
