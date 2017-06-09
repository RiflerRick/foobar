"""
This was the most naive approach i had applied. It is giving a wrong solution.
"""


def answer(maze):
    obj=BunnyEscape(maze)
    obj.trackPath(0, 0, 0, 0)
    obj.printResult()
    
    # print((len(maze)+(len(maze[0])))-1)

class BunnyEscape:
    def __init__(self, maze):
        self.pathNodes=0
        self.maze=maze
        self.maxRow=len(maze)
        self.maxCol=len(maze[0])
        self.stopExecution=0
        self.foundFirstPath=0

    def printResult(self):
        print(self.pathNodes)
    def trackPath(self, row, col, countNodes, isWallBroken):
        # print('row:' +str(row)+ ' col: '+str(col)+ ' countNodes: '+str(countNodes))
        if self.foundFirstPath==1:
            # if countNodes+1 > self.pathNodes:
            #     print('countNodes+1 > pathNodes')
                return 
        if row==self.maxRow-1 and col==self.maxCol-1:
            if self.foundFirstPath==0:
                self.foundFirstPath=1
                self.pathNodes=countNodes+1
                # print('reached end')
                return
            # else:
            #     # it means that the countNodes + 1 value is definitely less than pathNodes otherwise it would not have come here
            #     print('here we go again')
            #     self.pathNodes=countNodes+1
        else:
            if row==self.maxRow-1:
                if self.maze[row][col]==1:
                    # passage is not allowed until changed
                    if isWallBroken==1:
                        return countNodes-1
                    else:
                        isWallBroken=1
                countNodes+=1
                self.trackPath(row, col+1, countNodes, isWallBroken)

            elif col==self.maxCol-1:
                if self.maze[row][col]==1:
                    # passage is not allowed until changed
                    if isWallBroken==1:
                        return countNodes-1
                    else:
                        isWallBroken=1
                countNodes+=1
                self.trackPath(row+1, col, countNodes, isWallBroken)
            else:
                if self.maze[row][col]==1:
                    if isWallBroken==1:
                        return countNodes-1
                    else:
                        isWallBroken=1
                countNodes+=1
                self.trackPath(row+1, col, countNodes, isWallBroken)
                self.trackPath(row, col+1, countNodes, isWallBroken)


answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])