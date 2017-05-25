class Node:
    
    def __init__(self):
        # self.data=0
        self.right=None
        self.left=None
    
    # getter and setter methods for left, right pointers and data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    # def getData(self):
    #     return self.data
    
    def setRight(self, right):
        self.right=right

    def setLeft(self, left):
        self.left=left

    # def setData(self, data):
        # self.data=data

class BinaryTree:
        
    def __init__(self, h):
        self.height=h
        self.root=Node()
        self.root.setLeft(None)
        self.root.setRight(None)
        # self.root.setData(-1)
        self.count=1

    # def printBinaryTree(self):
        
    #     self.printNode(self.root)

    def createBinaryTree(self):
        
        self.createNode(self.root, 0 ,self.height-1)
        self.createNode(self.root, 1, self.height-1)

    # def printNode(self, node):
    #     if node==None:
    #         return 
        
    #     self.printNode(node.getLeft())
    #     # print("  ", end="")
    #     self.printNode(node.getRight())
    #     # print()
    #     print(node.getData(), end="")

    # h is the height of the binary tree - 1
    def createNode(self, prevNode, side, h): 
        if h==0:
            return 
        node=Node()
        node.setLeft(None)
        node.setRight(None)
        # node.setData(-1)
        if side==0: 
            # meaning left
            prevNode.setLeft(node)
        else:
            prevNode.setRight(node)
        self.createNode(node, 0, h-1)
        self.createNode(node, 1, h-1)


    def postOrder(self, node):
        if node==None:
            return
        self.postOrder(node.getLeft())
        self.postOrder(node.getRight())
        self.setValue(node)

    def setCount(self, count):
        self.count=count

    # def setValue(self, node):
    #     node.setData(self.count)
    #     self.count+=1

def main():
    obj=BinaryTree(30)
    # obj=BinaryTree(h)# giving the height of the binary tree as 3
    obj.createBinaryTree()
    # obj.postOrder(obj.root)

if __name__=="__main__":
    main()