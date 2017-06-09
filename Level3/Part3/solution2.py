"""
It seems that the go to solution in this case is a BFS and not a DFS. Unfortunately in the previous solution I was going for a DFS algorithm and it was not working. Lets now go for a BFS and see if it works.

This one is just a basic BFS algorithm... it unfortunately, does not work where we can change one single 
"""
def answer(maze):
    obj=BunnyEscape(maze)
    obj.printPath()

class BunnyEscape:
    
    def __init__(self, maze):
        self.queue=[(0,0)]
        self.maze=maze
        self.maxRow=len(maze)-1
        self.maxCol=len(maze[0])-1
        self.weights={}
        # self.walls=[]
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                # if self.maze[(i,j)]==1:
                    # self.walls.append((i,j))
                self.weights[(i,j)]=1000000 # this is just assignment of weights
        self.weights[(0,0)]=1

    def trackPath(self, row, col):        

        if row==self.maxRow and col==self.maxCol:
            return           

        if row==0 and col==0:
            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))
                
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))

        elif row < self.maxRow and col < self.maxCol and row > 0 and col > 0: # it means we are in the middle
            
            if self.maze[row-1][col]!=1: # top
                if self.weights[(row, col)]+1 <= self.weights[(row-1,col)]:
                    self.weights[(row-1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row-1,col))

            if self.maze[row][col-1]!=1: # left
                if self.weights[(row, col)]+1 <= self.weights[(row,col-1)]:
                    self.weights[(row, col-1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col-1))

            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))
                
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))

        # lets handle corners
        elif row == 0 and col == self.maxCol:
            
            # you can go left and down
            if self.maze[row][col-1]!=1: # left
                if self.weights[(row, col)]+1 <= self.weights[(row,col-1)]:
                    self.weights[(row, col-1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col-1))

            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))

        elif col==0 and row==self.maxRow:
            
            # you can go top and right
            if self.maze[row-1][col]!=1: # top
                if self.weights[(row, col)]+1 <= self.weights[(row-1,col)]:
                    self.weights[(row-1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row-1,col))
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))

        elif row == 0: # three directions: down, left and right
            
            if self.maze[row][col-1]!=1: # left
                if self.weights[(row, col)]+1 <= self.weights[(row,col-1)]:
                    self.weights[(row, col-1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col-1))

            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))
                
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))

        elif col == 0: # three directions: down, top and right

            if self.maze[row-1][col]!=1: # top
                if self.weights[(row, col)]+1 <= self.weights[(row-1,col)]:
                    self.weights[(row-1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row-1,col))
            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))
                
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))

        elif col == self.maxCol:
            # you can go top , down and left
            if self.maze[row-1][col]!=1: # top
                if self.weights[(row, col)]+1 <= self.weights[(row-1,col)]:
                    self.weights[(row-1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row-1,col))
            if self.maze[row+1][col]!=1: # down
                if self.weights[(row, col)]+1 <= self.weights[(row+1,col)]:
                    self.weights[(row+1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row+1,col))
            if self.maze[row][col-1]!=1: # left
                if self.weights[(row, col)]+1 <= self.weights[(row,col-1)]:
                    self.weights[(row, col-1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col-1))

        else:
            # you can go left right and top
            if self.maze[row][col-1]!=1: # left
                if self.weights[(row, col)]+1 <= self.weights[(row,col-1)]:
                    self.weights[(row, col-1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col-1)) 
            if self.maze[row-1][col]!=1: # top
                if self.weights[(row, col)]+1 <= self.weights[(row-1,col)]:
                    self.weights[(row-1, col)]=self.weights[(row,col)]+1
                    self.queue.append((row-1,col))
            if self.maze[row][col+1]!=1: # right
                if self.weights[(row,col)]+1 <= self.weights[(row, col+1)]:
                    self.weights[(row, col+1)]=self.weights[(row,col)]+1
                    self.queue.append((row,col+1))           

    def printPath(self):
        
        while self.queue != []:
            # print ('queue now: '+str(self.queue))
            node=self.queue.pop(0)
            row=node[0]
            col=node[1]
            self.trackPath(row, col)

        print('printing all weights: ----')
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                print(str(self.weights[(i,j)]) + '\t',end='')
            print()

        print(self.weights[(len(self.maze)-1, len(self.maze[0])-1)])

answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])