from collections import deque
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


class Traversal:
    def inorder(self, root, traversal):
        if root:
            # inorder traversal of left sub-tree
            self.inorder(root.left, traversal)

            traversal.append(root.val)

            # inorder traversal of right sub-tree
            self.inorder(root.right, traversal)

        return traversal


    def inorder_iterative(self, root):
        if not root:
            return []

        # inorder traversal list
        traversal = []

        # node stack
        nodestack = deque([])
        while True:
            if root:
                nodestack.append(root)
                root = root.left
            else:
                if len(nodestack) == 0:
                    break

                p = nodestack.pop()
                traversal.append(p.val)

                root = p.right

        return traversal

    def preorder(self, root, traversal):
        if root:
            # add root value to the traversal list
            traversal.append(root.val)

            # preorder on left subtree
            self.preorder(root.left, traversal)

            # preorder on right subtree
            self.preorder(root.right, traversal)

    def preorder_iterative(self, root):
        traversal = []

        nodestack = deque([root])
        while(nodestack):
            p = nodestack.pop()

            # add the parent to the traversal list
            traversal.append(p.val)

            if p.right:
                nodestack.append(p.right)

            if p.left:
                nodestack.append(p.left)

        return traversal


    def postorder(self, root, traversal):
        if root:
            # post order of left child
            self.postorder(root.left, traversal)

            # post order of the right child
            self.postorder(root.right, traversal)

            traversal.append(root.val)

    def postorder_iterative(self, root):
        # one stack solution
        if not root:
            return []

        traversal, current = [], root

        # create an empty stack
        nodestack = deque([])

        while(current or len(nodestack) > 0):
            if current:
                nodestack.append(current)
                current = current.left
            else:
                # if current is null, peek at the last node added to the stack
                # check if it has a right child, if it doesnt then visit it
                if not nodestack[-1].right:
                    # leaf node
                    l = nodestack.pop()
                    traversal.append(l.val)

                    # while the last popped node from stack was a right child
                    # keep popping
                    while nodestack and nodestack[-1].right == l:
                        l = nodestack.pop()
                        traversal.append(l.val)

                else:
                    # if it has a right child, move right
                    current = nodestack[-1].right

        return traversal

class Morris:
    def inorder(self, root):
        traversal = []

        current = root
        while current:
            if not current.left:
                traversal.append(current.val)
                current = current.right
            else:
                predecessor = self.findpredecessor(current)

                if not predecessor.right:
                    # morris link from right most descendent of left subtree to current
                    predecessor.right = current
                    current = current.left
                else:
                    # remove morris link from right most descendent of left subtree to current
                    predecessor.right = None
                    traversal.append(current.val)
                    current = current.right

        return traversal

    def preorder(self, root):
        traversal = []

        current = root
        while current:
            if not current.left:
                traversal.append(current.val)
                current = current.right
            else:
                predecessor = self.findpredecessor(current)

                if not predecessor.right:
                    # morris link from right most descendent of left subtree to current
                    predecessor.right = current
                    traversal.append(current.val)
                    current = current.left
                else:
                    # remove morris link from right most descendent of left subtree to current
                    predecessor.right = None
                    current = current.right

        return traversal

    def findpredecessor(self, current):
        predec = current.left

        while(True):
            if not predec.right or predec.right == current:
                break
            else:
                predec = predec.right

        return predec




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    ############### Traversal ################
    print("INORDER TRAVERSAL")
    t = Traversal()
    print(t.inorder(root, []))
    print(t.inorder_iterative(root))

    print("PREORDER TRAVERSAL")
    trvsl = []
    t.preorder(root, trvsl)
    print(trvsl)
    print(t.preorder_iterative(root))

    print("POSTORDER TRAVERSAL")
    trvsl = []
    t.postorder(root, trvsl)
    print(trvsl)

    print(t.postorder_iterative(root))

    ############### Morris Traversal ################
    m = Morris()
    print("INORDER TRAVERSAL")
    print(m.inorder(root))
    print("PREORDER TRAVERSAL")
    print(m.preorder(root))


