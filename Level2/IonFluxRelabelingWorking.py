import math
ans=[]
query=[]
def answer(h,q):
    query=q
    if h>15:
        # constructs trees of height 2^15 at each step, find the q elements in that step itself and store the root of 
        # each of the trees of height 15 in a list and construct the upper tree from  there deleting the previous trees

        # An optimization can be to know the roots of every second tree. That way still we can figure out what will be the upper # node
        upperTreeHeight=h-15
        numLowerTrees=int(math.pow(2,upperTreeHeight))
        lowerRoots=[] # stores roots of every second lower tree
        start=1
        skipSequence=buildSkippingSequence(numLowerTrees)
        for i in range(numLowerTrees):
            obj=BinaryTree(15)
            obj.createBinaryTree()
            obj.setStart(start)
            # print("start now: at i "+str(i) + ", " + str(start))
            
            obj.postOrder(obj.root) # start represents the initial value to start'
            # print("root now: at i "+str(i)+", "+str(obj.root.getData()))
            if i!=numLowerTrees-1:
                start=obj.root.getData()+skipSequence[i]
                # print("start now:"+str(start))# DEBUG
            # print("checking")
            checkLargeTree(obj, query, 15, int(math.pow(2,15+i)-1), 0)
            # if i%2==1:
            lowerRoots.append(obj.root.getData())
            # print("lowerAlternateRoots:"+str(lowerAlternateRoots)) #DEBUG
            del obj
        # coming to the upper tree
        obj=BinaryTree(upperTreeHeight+1)
        obj.createBinaryTree()
        # print(lowerRoots)
        obj.assignLeaves(obj.root, lowerRoots)
        obj.printLeaves(obj.root) # DEBUG

        # now the data of these trees will be assigned differently 
        obj.postOrderUpperTree(obj.root)
        # print("post order applied")
        obj.printLeaves(obj.root) # DEBUG
        checkLargeTree(obj, q, upperTreeHeight+1, int(math.pow(2,h))-1, 1)

    else:
        
        obj=BinaryTree(h)# giving the height of the binary tree as <15
        obj.createBinaryTree()
        obj.postOrder(obj.root)
        checkSmallTree(obj, q, h)
        # obj.printBinaryTree()
        # print()
        # ans=[]
        del obj
    # return ans
    print(ans)

def buildSkippingSequence(numLowerTrees):
    l=[0 for i in range(int(numLowerTrees)-1)]
    midValue=int(math.log(numLowerTrees, 2))
    populateSequence(0, len(l)-1, l, midValue)
    return l

def populateSequence(start, end, l, midValue):
    # print("midValue now:"+str(midValue))
    if midValue==0:
        return
    # print("start: "+str(start))
    # print("end: "+str(end))
    mid=int((end+start)/2)
    l[mid]=midValue
    populateSequence(start, mid, l, midValue-1)
    populateSequence(mid+1, end, l, midValue-1)

def checkSmallTree(obj, q, h):
    for i in q:
        if i >= (int(math.pow(2,h))-1):
            ans.append(-1)
            # continue
        else:
            ionRelabel(None, obj.root, i)
            # q.remove(i)

def checkLargeTree(obj, q, h, upperLimit, upperTree):
    for i in q:
        # print("i now:"+str(i))
        if i >= upperLimit:
            # ans.append(-1)
            if upperTree==0:
                continue
            else:
                ans.append(-1)
        else:
            # print("found:"+str(i))
            ionRelabel(None, obj.root, i)
            # q.remove(i)
            # print("printing q:"+str(q))

def ionRelabel(prev, node, num):
    if node==None:
        return
    ionRelabel(node, node.getLeft(), num)
    ionRelabel(node, node.getRight(), num)
    if node.getData()==num:
        
        ans.append(prev.getData())
        # print ("ans now: "+str(ans))

class Node:

    def __init__(self):
        self.data=0
        self.right=None
        self.left=None
    
    # getter and setter methods for left, right pointers and data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getData(self):
        return self.data
    
    def setRight(self, right):
        self.right=right

    def setLeft(self, left):
        self.left=left

    def setData(self, data):
        self.data=data

class BinaryTree:
        
    def __init__(self, h):
        self.height=h
        self.root=Node()
        self.root.setLeft(None)
        self.root.setRight(None)
        self.root.setData(-1)
        self.start=1
        self.index=0

    def printBinaryTree(self):
        
        self.printNode(self.root)

    def createBinaryTree(self):
        
        self.createNode(self.root, 0 ,self.height-1)
        self.createNode(self.root, 1, self.height-1)

    def printNode(self, node):
        if node==None:
            return 
        
        self.printNode(node.getLeft())
        # print("  ", end="")
        self.printNode(node.getRight())
        # print()
        # print(node.getData(), end="")

    # h is the height of the binary tree - 1
    def createNode(self, prevNode, side, h): 
        if h==0:
            return 
        node=Node()
        node.setLeft(None)
        node.setRight(None)
        node.setData(-1)
        if side==0: 
            # meaning left
            prevNode.setLeft(node)
        else:
            prevNode.setRight(node)
        self.createNode(node, 0, h-1)
        self.createNode(node, 1, h-1)

    def printLeaves(self, node):
        if node.getLeft()==None and node.getRight()==None:
            # print("val:"+str(node.getData()))
            return
        self.printLeaves(node.getLeft())
        self.printLeaves(node.getRight())
        return

    def setLeaf(self, node, lowerIndex):
        node.setData(lowerIndex[self.index])
        self.index+=1

    def assignLeaves(self, node, lowerRoots):
        if node.getLeft()==None and node.getRight()==None:
            self.setLeaf(node, lowerRoots)
            return
        self.assignLeaves(node.getLeft(), lowerRoots)
        self.assignLeaves(node.getRight(), lowerRoots)
        return
        

    def goRight(self, node):
        if node.getLeft()==None:
            # print ("data right:"+str(node.getData()))
            return node.getData()
        data=self.goRight(node.getRight())
        # print("setting data"+str(data+1))
        node.setData(data+1)
        return data+1

    def postOrderUpperTree(self, node):
        while node.getLeft()!=None:
            self.goRight(node)
            node=node.getLeft()

    def postOrder(self, node):
        if node==None:
            return
        self.postOrder(node.getLeft())
        self.postOrder(node.getRight())
        self.setValue(node)

    def setData(self, node, data):
        node.data=data

    def setStart(self, start):
        self.start=start

    def setValue(self, node):
        node.setData(self.start)
        self.start+=1

    
def main():
    # count=1
    # obj=BinaryTree(3)# giving the height of the binary tree as 3
    # obj.createBinaryTree()
    # obj.postOrder(obj.root)
    # obj.printBinaryTree()
    answer(25, [19, 14, 28, 32767])

if __name__=="__main__":
    main()
